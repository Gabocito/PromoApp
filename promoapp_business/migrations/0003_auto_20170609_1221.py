# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-09 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('promoapp_business', '0002_auto_20170609_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyAdvertisingCampaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertisingcampaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promoapp_business.AdvertisingCampaign')),
            ],
        ),
        migrations.AlterField(
            model_name='company',
            name='is_active',
            field=models.BooleanField(),
        ),
        migrations.RemoveField(
            model_name='promotion',
            name='products',
        ),
        migrations.AddField(
            model_name='promotion',
            name='products',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.AddField(
            model_name='companyadvertisingcampaign',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promoapp_business.Company'),
        ),
        migrations.AddField(
            model_name='companyadvertisingcampaign',
            name='promotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='promoapp_business.Promotion'),
        ),
        migrations.AddField(
            model_name='company',
            name='advertisingcampaigns',
            field=models.ManyToManyField(through='promoapp_business.CompanyAdvertisingCampaign', to='promoapp_business.AdvertisingCampaign'),
        ),
    ]
