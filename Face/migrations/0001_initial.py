# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-19 15:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Face_main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=b'')),
                ('predicted_age', models.CharField(max_length=5)),
            ],
        ),
    ]
