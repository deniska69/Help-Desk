# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivc', '0008_auto_20170618_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='abb',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
    ]
