# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoapp_user', '0012_auto_20170622_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='promotionmanager',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='storemanager',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
