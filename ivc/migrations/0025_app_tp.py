# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 21:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ivc', '0024_auto_20170618_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='tp',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ivc.Type_App'),
        ),
    ]