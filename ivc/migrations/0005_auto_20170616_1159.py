# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-16 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ivc', '0004_app_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='lab_logo',
            field=models.FileField(upload_to=''),
        ),
    ]