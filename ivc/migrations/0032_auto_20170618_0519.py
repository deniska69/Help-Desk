# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 22:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ivc', '0031_app_date2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app',
            name='st',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ivc.Status'),
        ),
    ]