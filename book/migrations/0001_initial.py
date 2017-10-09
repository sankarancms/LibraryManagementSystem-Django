# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
            ],
        ),
    ]
