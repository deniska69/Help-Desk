# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ivc', '0038_auto_20170618_0603'),
    ]

    operations = [
        migrations.RenameField(
            model_name='app',
            old_name='em1',
            new_name='em',
        ),
    ]