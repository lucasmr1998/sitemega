import csv

from django.contrib import admin
from django.http import HttpResponse

from .models import Lead


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('nome', 'source', 'celular', 'email', 'created_at', 'webhook_sent')
    list_filter = ('source', 'webhook_sent', 'created_at')
    search_fields = ('nome', 'email', 'celular', 'cpf')
    readonly_fields = ('created_at', 'ip_address', 'webhook_sent')
    date_hierarchy = 'created_at'
    list_per_page = 30

    actions = ['export_csv']

    @admin.action(description='Exportar CSV')
    def export_csv(self, request, queryset):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="leads.csv"'
        writer = csv.writer(response)
        writer.writerow(['Nome', 'Email', 'Celular', 'CPF', 'Origem', 'Data'])
        for lead in queryset:
            writer.writerow([
                lead.nome, lead.email, lead.celular, lead.cpf,
                lead.source, lead.created_at.strftime('%d/%m/%Y %H:%M'),
            ])
        return response
