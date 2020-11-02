# Generated by Django 3.1.2 on 2020-11-02 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('id_zone', models.CharField(max_length=100, unique=True, verbose_name='Código zona')),
                ('location', models.TextField(verbose_name='Ubicación')),
                ('soil_type', models.CharField(max_length=100, verbose_name='Tipo de suelo')),
                ('size', models.CharField(max_length=100, verbose_name='Tamaño')),
                ('state', models.CharField(max_length=100, verbose_name='Estado')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]