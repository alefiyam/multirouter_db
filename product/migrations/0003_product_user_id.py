# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-09-12 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20170912_0435'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='user_id',
            field=models.IntegerField(default=None),
        ),
    ]