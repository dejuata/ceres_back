# Generated by Django 3.1.2 on 2020-11-18 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0003_schedule_codigo_zona'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='nombre_labor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
