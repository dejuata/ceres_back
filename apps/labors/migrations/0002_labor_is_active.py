# Generated by Django 3.1.2 on 2020-12-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='labor',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]