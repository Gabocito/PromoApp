# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-23 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoapp_campaign', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisingcampaign',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='advertisingcampaign',
            name='promotions',
            field=models.ManyToManyField(to='promoapp_campaign.Promotion'),
        ),
    ]
