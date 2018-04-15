# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 13:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('minimum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GuildMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(blank=True, default=None, max_length=64, null=True)),
                ('force', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='minimum.Minimum')),
            ],
        ),
    ]