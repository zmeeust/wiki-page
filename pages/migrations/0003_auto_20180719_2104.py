# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-07-19 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20180719_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='version',
            name='current_page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='versions', to='pages.Page'),
        ),
    ]
