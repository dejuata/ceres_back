# Generated by Django 3.1.2 on 2020-12-10 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
