# Generated by Django 3.1.2 on 2020-11-20 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zone',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]