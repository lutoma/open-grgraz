# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 11:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20160728_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='motion_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='motion',
            name='motion_id',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='motion',
            name='motion_type',
            field=models.CharField(default='', max_length=200),
        ),
    ]
