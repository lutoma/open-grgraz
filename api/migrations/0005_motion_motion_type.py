# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-28 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160728_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='motion',
            name='motion_type',
            field=models.CharField(default=None, max_length=200, null=True),
        ),
    ]
