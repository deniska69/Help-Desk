# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-17 19:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ivc', '0006_housing'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_cr', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=250)),
                ('housing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ivc.Housing')),
            ],
        ),
    ]
