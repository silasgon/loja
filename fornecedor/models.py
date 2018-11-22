from django.db import models

# Create your models here.


class Fornecedor(models.Model):
    name = models.CharField(max_length=100, blank=False, verbose_name='Nome')
    phone = models.CharField(max_length=20, blank=False, verbose_name='Telefone')
    email = models.CharField(max_length=200, blank=True, verbose_name='Email')
    adress = models.CharField(max_length=200, blank=True, verbose_name='Endereço')
    city = models.CharField(max_length=100, blank=True, verbose_name='Cidade')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.name, str(self.phone)
