# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivc', '0040_app_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='username',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
