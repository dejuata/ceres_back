from django.db import models
from apps.utils.models import AbstractTableMeta
from apps.zones.models import Zone
from apps.labors.models import Labor
from apps.authentication.models import User


class Schedule(AbstractTableMeta, models.Model):
    schedule_date = models.DateField(auto_now=False, auto_now_add=False, null=False, blank=False, verbose_name="Fecha")
    start_hour = models.TimeField(null=True, blank=True, verbose_name="Hora inicial")
    final_hour = models.TimeField(null=True, blank=True, verbose_name="Hora final")
    observation = models.TextField(null=True, blank=True, verbose_name="Observación")
    zone = models.ForeignKey(Zone, on_delete=models.DO_NOTHING, verbose_name="Zona de Campo")
    labor = models.ForeignKey(Labor, on_delete=models.DO_NOTHING, verbose_name="Labor de Campo")
    operator = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name="Operario")

    name_operator = models.CharField(max_length=100, null=True, blank=True)
    codigo_zona = models.CharField(max_length=100, null=True, blank=True)
    nombre_labor = models.CharField(max_length=100, null=True, blank=True)
    state = models.BooleanField(default=True, verbose_name="Estado")

    class Meta:
        verbose_name = "Programacion"

    def __str__(self):
        return str(self.id)
