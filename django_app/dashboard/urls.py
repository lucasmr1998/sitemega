from django.urls import path
from . import views
from . import builder_views

app_name = 'dashboard'

urlpatterns = [
    # Auth
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    # Dashboard
    path('', views.index, name='index'),
    path('config', views.config_view, name='config'),

    # Leads
    path('leads', views.leads_list, name='leads_list'),

    # Banners
    path('banners', views.banners_list, name='banners_list'),
    path('banners/novo', views.banners_form, name='banners_add'),
    path('banners/<int:pk>', views.banners_form, name='banners_edit'),
    path('banners/<int:pk>/excluir', views.banners_delete, name='banners_delete'),

    # Planos
    path('planos', views.plans_list, name='plans_list'),
    path('planos/novo', views.plans_form, name='plans_add'),
    path('planos/<int:pk>', views.plans_form, name='plans_edit'),
    path('planos/<int:pk>/excluir', views.plans_delete, name='plans_delete'),

    # Combos
    path('combos', views.combos_list, name='combos_list'),
    path('combos/novo', views.combos_form, name='combos_add'),
    path('combos/<int:pk>', views.combos_form, name='combos_edit'),
    path('combos/<int:pk>/excluir', views.combos_delete, name='combos_delete'),

    # Serviços
    path('servicos', views.services_list, name='services_list'),
    path('servicos/novo', views.services_form, name='services_add'),
    path('servicos/<int:pk>', views.services_form, name='services_edit'),
    path('servicos/<int:pk>/excluir', views.services_delete, name='services_delete'),

    # Autoatendimento
    path('autoatendimento', views.selfservice_list, name='selfservice_list'),
    path('autoatendimento/novo', views.selfservice_form, name='selfservice_add'),
    path('autoatendimento/<int:pk>', views.selfservice_form, name='selfservice_edit'),
    path('autoatendimento/<int:pk>/excluir', views.selfservice_delete, name='selfservice_delete'),

    # App
    path('app', views.app_list, name='app_list'),
    path('app/novo', views.app_form, name='app_add'),
    path('app/<int:pk>', views.app_form, name='app_edit'),
    path('app/<int:pk>/excluir', views.app_delete, name='app_delete'),

    # Menus
    path('menus', views.menus_list, name='menus_list'),
    path('menus/novo', views.menus_form, name='menus_add'),
    path('menus/<int:pk>', views.menus_form, name='menus_edit'),
    path('menus/<int:pk>/excluir', views.menus_delete, name='menus_delete'),

    # Footer
    path('rodape', views.footer_list, name='footer_list'),
    path('rodape/novo', views.footer_form, name='footer_add'),
    path('rodape/<int:pk>', views.footer_form, name='footer_edit'),
    path('rodape/<int:pk>/excluir', views.footer_delete, name='footer_delete'),

    # Energia (singleton)
    path('energia', views.energia_view, name='energia'),

    # Rastreamento (singleton)
    path('rastreamento', views.rastreamento_view, name='rastreamento'),

    # Page Builder
    path('paginas', builder_views.pages_list, name='pages_list'),
    path('paginas/nova', builder_views.page_form, name='page_add'),
    path('paginas/<int:pk>', builder_views.page_form, name='page_edit'),
    path('paginas/<int:pk>/excluir', builder_views.page_delete, name='page_delete'),
    path('paginas/<int:pk>/editor', builder_views.page_editor, name='page_editor'),
    path('paginas/<int:pk>/componente/novo', builder_views.component_add, name='component_add'),
    path('paginas/componente/<int:pk>/editar', builder_views.component_edit, name='component_edit'),
    path('paginas/componente/<int:pk>/excluir', builder_views.component_delete, name='component_delete'),
    path('paginas/<int:pk>/reordenar', builder_views.component_reorder, name='component_reorder'),
    path('componentes', builder_views.components_list, name='components_list'),
]
