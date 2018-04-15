# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-19 11:57
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minimum', '0011_auto_20180310_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ads', ckeditor.fields.RichTextField(blank=True, default=None, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]