# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-25 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bg_result', '0007_remove_bgresult_force_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Minimumm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('force', models.IntegerField(default=1)),
                ('minimum', models.IntegerField(default=1)),
            ],
        ),
    ]