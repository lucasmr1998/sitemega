from django.db import models


class Lead(models.Model):
    SOURCE_CHOICES = [
        ('energia', 'Energia'),
        ('rastreamento', 'Rastreamento'),
        ('internet', 'Internet'),
        ('geral', 'Geral'),
    ]

    source = models.CharField('Origem', max_length=20, choices=SOURCE_CHOICES, default='geral')
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('E-mail', blank=True)
    celular = models.CharField('Celular', max_length=20, blank=True)
    cep = models.CharField('CEP', max_length=10, blank=True)
    media_conta = models.CharField('Média de conta de energia', max_length=100, blank=True)
    tipo_veiculo = models.CharField('Tipo de veículo', max_length=100, blank=True)
    cpf = models.CharField('CPF', max_length=14, blank=True)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IP', blank=True, null=True)
    webhook_sent = models.BooleanField('Webhook enviado', default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'

    def __str__(self):
        return f'{self.nome} ({self.source}) - {self.created_at:%d/%m/%Y}'
