from django.db import models
from apps.utils.models import AbstractTableMeta


class Labor(AbstractTableMeta, models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre")
    description = models.TextField(verbose_name="Descripción")
    labor_type = models.CharField(max_length=100, verbose_name="Tipo de Labor")
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Zona de Campo"

    def __str__(self):
        return self.name
