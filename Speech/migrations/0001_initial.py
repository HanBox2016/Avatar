# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Speech_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.CharField(max_length=255)),
                ('sentiments', models.CharField(max_length=20)),
                ('dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]