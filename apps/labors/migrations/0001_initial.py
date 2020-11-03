# Generated by Django 3.1.2 on 2020-11-03 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Labor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('labor_type', models.CharField(max_length=100, verbose_name='Tipo de Labor')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
