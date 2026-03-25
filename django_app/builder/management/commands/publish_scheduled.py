from django.core.management.base import BaseCommand
from django.utils import timezone

from builder.models import Page


class Command(BaseCommand):
    help = 'Publica/despublica páginas agendadas'

    def handle(self, *args, **options):
        now = timezone.now()

        # Publicar agendadas
        scheduled = Page.objects.filter(status='scheduled', publish_at__lte=now)
        pub_count = scheduled.update(status='published')
        if pub_count:
            self.stdout.write(f'{pub_count} página(s) publicada(s)')

        # Despublicar expiradas
        expired = Page.objects.filter(
            status='published',
            unpublish_at__isnull=False,
            unpublish_at__lte=now,
        )
        unpub_count = expired.update(status='draft', unpublish_at=None)
        if unpub_count:
            self.stdout.write(f'{unpub_count} página(s) despublicada(s)')

        if not pub_count and not unpub_count:
            self.stdout.write('Nenhuma alteração.')
