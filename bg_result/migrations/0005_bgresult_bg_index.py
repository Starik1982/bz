# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bg_result', '0004_auto_20171225_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='bgresult',
            name='bg_index',
            field=models.IntegerField(default=1),
        ),
    ]