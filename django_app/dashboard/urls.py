from django.urls import path
from . import views
from . import builder_views
from media_library import views as media_views
from shortener import dashboard_views as shortener_views

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
    path('paginas/<int:pk>/preview', builder_views.page_preview, name='page_preview'),
    path('paginas/<int:pk>/duplicar', builder_views.page_duplicate, name='page_duplicate'),
    path('paginas/componente/<int:pk>/autosave', builder_views.component_autosave, name='component_autosave'),
    path('paginas/componente/<int:pk>/duplicar', builder_views.component_duplicate, name='component_duplicate'),
    path('paginas/<int:pk>/revisoes', builder_views.revision_list, name='revision_list'),
    path('paginas/<int:pk>/revisoes/<int:rev_pk>/restaurar', builder_views.revision_restore, name='revision_restore'),
    path('componentes', builder_views.components_list, name='components_list'),

    # Templates
    path('templates', builder_views.templates_list, name='templates_list'),
    path('paginas/<int:pk>/salvar-template', builder_views.template_save, name='template_save'),
    path('templates/<int:pk>/aplicar', builder_views.template_apply, name='template_apply'),
    path('templates/<int:pk>/excluir', builder_views.template_delete, name='template_delete'),

    # Import / Export
    path('paginas/<int:pk>/exportar', builder_views.page_export, name='page_export'),
    path('paginas/importar', builder_views.page_import, name='page_import'),

    # Analytics
    path('analytics', builder_views.analytics_view, name='analytics'),

    # Shortener
    path('links', shortener_views.links_list, name='links_list'),
    path('links/novo', shortener_views.link_form, name='link_add'),
    path('links/<int:pk>', shortener_views.link_form, name='link_edit'),
    path('links/<int:pk>/excluir', shortener_views.link_delete, name='link_delete'),
    path('links/<int:pk>/stats', shortener_views.link_stats, name='link_stats'),

    # Media Library
    path('media', media_views.media_list, name='media_list'),
    path('media/upload', media_views.media_upload, name='media_upload'),
    path('media/<int:pk>/excluir', media_views.media_delete, name='media_delete'),
    path('media/browse', media_views.media_browse, name='media_browse'),
]
