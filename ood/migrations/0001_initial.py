# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 22:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OODBeispiel',
            fields=[
                ('beispielsatz', models.CharField(max_length=300, verbose_name='Beispiel Satz')),
                ('bsp_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
