# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-11 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0016_auto_20171011_0449'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': '장소', 'verbose_name_plural': '장소 목록'},
        ),
        migrations.AlterField(
            model_name='place',
            name='name',
            field=models.CharField(db_index=True, max_length=50),
        ),
    ]
