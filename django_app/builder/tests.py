from django.test import Client, TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from builder.models import Page, ComponentType, PageComponent


def make_user():
    user = User.objects.create_superuser('test', 'test@test.com', 'pass')
    return user


def make_page(**kwargs):
    defaults = {'title': 'Teste', 'slug': 'teste', 'status': 'draft'}
    defaults.update(kwargs)
    return Page.objects.create(**defaults)


def make_component_type(**kwargs):
    defaults = {
        'name': 'Hero',
        'slug': 'hero',
        'template_name': 'components/hero.html',
        'schema': [{'name': 'title', 'type': 'text', 'label': 'Título'}],
    }
    defaults.update(kwargs)
    return ComponentType.objects.create(**defaults)


# ─── Model tests ──────────────────────────────────────────────────────────────

class PageModelTest(TestCase):
    def test_str(self):
        page = make_page()
        self.assertEqual(str(page), 'Teste')

    def test_slug_unique(self):
        make_page(slug='unico')
        with self.assertRaises(Exception):
            make_page(slug='unico')

    def test_get_absolute_url(self):
        page = make_page(slug='minha-pagina')
        self.assertIn('minha-pagina', page.get_absolute_url())


class ComponentTypeModelTest(TestCase):
    def test_slug_auto_generated(self):
        ct = ComponentType.objects.create(
            name='Meu Hero',
            template_name='components/hero.html',
            schema=[],
        )
        self.assertEqual(ct.slug, 'meu-hero')

    def test_str(self):
        ct = make_component_type()
        self.assertEqual(str(ct), 'Hero')


# ─── View tests ───────────────────────────────────────────────────────────────

class BuilderViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = make_user()
        self.client.login(username='test', password='pass')
        self.page = make_page()
        self.ct = make_component_type()

    def test_pages_list(self):
        res = self.client.get(reverse('dashboard:pages_list'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, 'Teste')

    def test_page_editor(self):
        res = self.client.get(reverse('dashboard:page_editor', kwargs={'pk': self.page.pk}))
        self.assertEqual(res.status_code, 200)

    def test_visual_editor(self):
        res = self.client.get(reverse('dashboard:visual_editor', kwargs={'pk': self.page.pk}))
        self.assertEqual(res.status_code, 200)

    def test_page_create(self):
        res = self.client.post(reverse('dashboard:page_add'), {
            'title': 'Nova Página',
            'slug': 'nova-pagina',
            'status': 'draft',
            'meta_description': '',
        })
        self.assertTrue(Page.objects.filter(slug='nova-pagina').exists())

    def test_page_delete(self):
        page = make_page(slug='deletar')
        res = self.client.post(reverse('dashboard:page_delete', kwargs={'pk': page.pk}))
        self.assertFalse(Page.objects.filter(pk=page.pk).exists())

    def test_component_add_ajax(self):
        res = self.client.post(
            reverse('dashboard:component_add', kwargs={'pk': self.page.pk}),
            {'component_type': self.ct.pk},
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertEqual(data['status'], 'ok')
        self.assertEqual(PageComponent.objects.filter(page=self.page).count(), 1)

    def test_component_delete_ajax(self):
        comp = PageComponent.objects.create(page=self.page, component_type=self.ct, data={}, order=0)
        res = self.client.post(
            reverse('dashboard:component_delete', kwargs={'pk': comp.pk}),
            HTTP_X_REQUESTED_WITH='XMLHttpRequest',
        )
        self.assertEqual(res.status_code, 200)
        self.assertFalse(PageComponent.objects.filter(pk=comp.pk).exists())

    def test_component_reorder(self):
        import json
        c1 = PageComponent.objects.create(page=self.page, component_type=self.ct, data={}, order=0)
        c2 = PageComponent.objects.create(page=self.page, component_type=self.ct, data={}, order=1)
        res = self.client.post(
            reverse('dashboard:component_reorder', kwargs={'pk': self.page.pk}),
            data=json.dumps([{'id': c1.pk, 'order': 1}, {'id': c2.pk, 'order': 0}]),
            content_type='application/json',
        )
        self.assertEqual(res.status_code, 200)
        self.assertEqual(PageComponent.objects.get(pk=c1.pk).order, 1)
        self.assertEqual(PageComponent.objects.get(pk=c2.pk).order, 0)

    def test_page_preview_iframe_allowed(self):
        res = self.client.get(reverse('dashboard:page_preview', kwargs={'pk': self.page.pk}))
        self.assertEqual(res.status_code, 200)
        self.assertNotIn('X-Frame-Options', res)

    def test_unauthenticated_redirects(self):
        self.client.logout()
        res = self.client.get(reverse('dashboard:pages_list'))
        self.assertEqual(res.status_code, 302)
