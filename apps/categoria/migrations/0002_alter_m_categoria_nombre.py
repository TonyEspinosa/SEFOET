# Generated by Django 4.2.7 on 2023-11-30 18:21

import apps.categoria.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categoria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='m_categoria',
            name='nombre',
            field=apps.categoria.models.UpperCharField(max_length=250, null=True, verbose_name='Nombre'),
        ),
    ]
