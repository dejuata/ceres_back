from django.db import models
from apps.utils.models import AbstractTableMeta

class Product(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre")
    brand = models.CharField(max_length=80, blank=True, null=True, verbose_name="Marca")
    model = models.CharField(max_length=80, blank=True, null=True, verbose_name="Modelo")
    serial = models.CharField(max_length=100, blank=False, null=False, verbose_name="Serial")
    type_pro = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo")
    date_purchase = models.DateField(blank=True, null=True, verbose_name="Fecha de compra", auto_now=True)
    cost = models.DecimalField(decimal_places=2,max_digits=10, blank=True, null=True, verbose_name="Costo", default=0)
    quantity = models.IntegerField(null=True, blank=True, verbose_name="Cantidad", default=0)
    state = models.BooleanField(default=True, verbose_name="Estado")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Zona de Campo"

    def __str__(self):
        return self.name
