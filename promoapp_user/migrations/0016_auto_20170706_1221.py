# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promoapp_user', '0015_auto_20170706_1202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='image',
        ),
        migrations.RemoveField(
            model_name='promotionmanager',
            name='image',
        ),
        migrations.RemoveField(
            model_name='storemanager',
            name='image',
        ),
        migrations.RemoveField(
            model_name='user',
            name='image',
        ),
    ]