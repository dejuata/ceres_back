# Generated by Django 3.1.2 on 2020-11-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]