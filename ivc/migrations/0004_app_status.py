# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-15 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivc', '0003_auto_20170531_1044'),
    ]

    operations = [
        migrations.AddField(
            model_name='app',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
