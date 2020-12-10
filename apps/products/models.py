from django.db import models
from apps.utils.models import AbstractTableMeta

class Product(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre")
    brand = models.CharField(max_length=80, blank=False, null=False, verbose_name="Marca")
    model = models.CharField(max_length=80, blank=False, null=False, verbose_name="Modelo")
    serial = models.CharField(max_length=100, blank=False, null=False, verbose_name="Serial")
    type_pro = models.CharField(max_length=100, blank=False, null=False, verbose_name="Tipo")
    date_purchase = models.DateField(blank=False, null=False, verbose_name="Fecha de compra")
    cost = models.DecimalField(decimal_places=2,max_digits=10, blank=False, null=False, verbose_name="Costo")
    state = models.IntegerField(blank=True, null=True, default=1)
    
    class Meta:
        verbose_name = "Zona de Campo"

    def __str__(self):
        return self.name
