# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 07:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='logo',
            field=models.CharField(max_length=200, null=True),
        ),
    ]