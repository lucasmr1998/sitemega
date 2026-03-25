from django.urls import path
from . import views
from . import builder_views
from media_library import views as media_views

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
    path('componentes', builder_views.components_list, name='components_list'),

    # Media Library
    path('media', media_views.media_list, name='media_list'),
    path('media/upload', media_views.media_upload, name='media_upload'),
    path('media/<int:pk>/excluir', media_views.media_delete, name='media_delete'),
    path('media/browse', media_views.media_browse, name='media_browse'),
]
