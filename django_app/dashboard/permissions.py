from functools import wraps

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden


# Role → permissions mapping
ROLE_PERMISSIONS = {
    'admin': {'*'},
    'editor': {
        'page.view', 'page.edit', 'page.create', 'page.delete',
        'component.edit', 'component.delete',
        'media.view', 'media.upload', 'media.delete',
        'lead.view', 'revision.view', 'revision.restore',
    },
    'viewer': {
        'page.view', 'lead.view', 'media.view', 'revision.view',
    },
}


def _user_has_permission(user, permission):
    if user.is_superuser:
        return True
    user_groups = set(user.groups.values_list('name', flat=True))
    for group_name in user_groups:
        perms = ROLE_PERMISSIONS.get(group_name, set())
        if '*' in perms or permission in perms:
            return True
    # Users with no group default to admin (backward compat)
    if not user_groups:
        return True
    return False


def role_required(permission):
    """Decorator that checks if user has the required permission via group roles."""
    def decorator(view_func):
        @wraps(view_func)
        @login_required(login_url='/painel/login')
        def _wrapped(request, *args, **kwargs):
            if not _user_has_permission(request.user, permission):
                return HttpResponseForbidden(
                    '<h1>Acesso negado</h1><p>Você não tem permissão para esta ação.</p>'
                )
            return view_func(request, *args, **kwargs)
        return _wrapped
    return decorator
