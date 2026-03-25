from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Cria os grupos de permissão (admin, editor, viewer)'

    def handle(self, *args, **options):
        for name in ('admin', 'editor', 'viewer'):
            group, created = Group.objects.get_or_create(name=name)
            status = 'criado' if created else 'já existe'
            self.stdout.write(f'  Grupo "{name}": {status}')
        self.stdout.write(self.style.SUCCESS('Grupos configurados!'))
