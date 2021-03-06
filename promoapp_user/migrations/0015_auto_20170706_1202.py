# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoapp_user', '0014_auto_20170628_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='storemanager',
            name='stores',
        ),
        migrations.AddField(
            model_name='admin',
            name='image',
            field=models.ImageField(default='anonymous.png', upload_to='profile_img/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='promotionmanager',
            name='image',
            field=models.ImageField(default='anonymous.png', upload_to='profile_img/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='storemanager',
            name='image',
            field=models.ImageField(default='anonymous.png', upload_to='profile_img/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='anonymous.png', upload_to='profile_img/'),
            preserve_default=False,
        ),
    ]
