from django.db import models
from apps.utils.models import AbstractTableMeta
from apps.schedules.models import Schedule


class Worklog(AbstractTableMeta, models.Model):
    actividad = models.ForeignKey(
        Schedule, on_delete=models.DO_NOTHING, verbose_name="Actividad")
    date = models.DateField(auto_now=False, auto_now_add=False,
                            null=False, blank=False, verbose_name="Fecha")
    description = models.TextField(null=True, blank=True, verbose_name="Descripción")
    # Evidencias
    file = models.FileField(blank=True, null=True, verbose_name="Imagen")
    audio = models.FileField(blank=True, null=True, verbose_name="Audio")
    lat = models.CharField(max_length=100, null=True, blank=True, verbose_name="Latitud")
    lng = models.CharField(max_length=100, null=True, blank=True, verbose_name="Longitud")

    name_operator = models.CharField(max_length=100, null=True, blank=True)
    codigo_zona = models.CharField(max_length=100, null=True, blank=True)
    nombre_labor = models.CharField(max_length=100, null=True, blank=True)
    state = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = "Bitácora"

    def __str__(self):
        return str(self.id)
