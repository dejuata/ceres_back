# Generated by Django 3.1.2 on 2020-11-18 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_schedule_name_operator'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='codigo_zona',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
