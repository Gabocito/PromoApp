# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-01 20:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoapp_user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='acc_type',
            field=models.CharField(default='', max_length=200),
        ),
    ]
