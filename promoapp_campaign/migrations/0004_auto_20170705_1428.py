# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-05 18:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promoapp_user', '0014_auto_20170628_1155'),
        ('promoapp_campaign', '0003_promotion_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisingcampaign',
            name='owner',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='promoapp_user.PromotionManager'),
        ),
        migrations.AddField(
            model_name='promotion',
            name='owner',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='promoapp_user.PromotionManager'),
        ),
    ]
