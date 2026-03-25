from django.core.management.base import BaseCommand
from builder.models import ComponentType
from builder.component_schemas import COMPONENT_SCHEMAS


class Command(BaseCommand):
    help = 'Cria/atualiza os tipos de componente a partir dos schemas'

    def handle(self, *args, **options):
        for slug, data in COMPONENT_SCHEMAS.items():
            obj, created = ComponentType.objects.update_or_create(
                slug=slug,
                defaults={
                    'name': data['name'],
                    'icon': data['icon'],
                    'description': data['description'],
                    'template_name': data['template'],
                    'schema': data['schema'],
                    'is_active': True,
                },
            )
            action = 'Criado' if created else 'Atualizado'
            self.stdout.write(f'  {action}: {obj.name}')

        self.stdout.write(self.style.SUCCESS(
            f'Total: {ComponentType.objects.count()} tipos de componente'
        ))
