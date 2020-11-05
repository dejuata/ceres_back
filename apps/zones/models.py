from django.db import models
from apps.utils.models import AbstractTableMeta


class Zone(AbstractTableMeta, models.Model):
    id_zone = models.CharField(max_length=100, blank=False, null=False, unique=True, verbose_name="Código zona")
    location = models.TextField(blank=False, null=False, verbose_name="Ubicación")
    soil_type = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tipo de suelo")
    size = models.CharField(max_length=100, blank=True, null=True, verbose_name="Tamaño")
    state = models.CharField(max_length=100, blank=True, null=True, verbose_name="Estado")

    class Meta:
        verbose_name = "Zona de Campo"

    def __str__(self):
        return self.id_zone
