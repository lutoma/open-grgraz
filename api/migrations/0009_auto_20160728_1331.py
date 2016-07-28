# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20160728_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='councilperson',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='long_filename',
            field=models.CharField(max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='motion',
            name='motion_id',
            field=models.IntegerField(default=-1, unique=True),
        ),
        migrations.AlterField(
            model_name='parliamentarysession',
            name='session_date',
            field=models.DateField(unique=True),
        ),
    ]