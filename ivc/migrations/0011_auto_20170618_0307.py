# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 20:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivc', '0010_auto_20170618_0306'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroom',
            old_name='id_hs',
            new_name='hs',
        ),
    ]
