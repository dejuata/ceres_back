from django.db import models
from apps.utils.models import AbstractTableMeta

class File(AbstractTableMeta, models.Model):
    emailFile = models.EmailField(verbose_name='Email')
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Nombre Labor")
    description = models.TextField(verbose_name="Descripción")
    file = models.FileField(blank=False, null=False)

    class Meta:
        verbose_name = "Bitácora"

    def __str__(self):
        return self.file.name
