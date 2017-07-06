# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-06 16:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('promoapp_user', '0018_auto_20170706_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='image',
            field=models.ImageField(default='profile_img/anonymous.png', upload_to='profile_img/'),
        ),
        migrations.AddField(
            model_name='promotionmanager',
            name='image',
            field=models.ImageField(default='profile_img/anonymous.png', upload_to='profile_img/'),
        ),
        migrations.AddField(
            model_name='storemanager',
            name='image',
            field=models.ImageField(default='profile_img/anonymous.png', upload_to='profile_img/'),
        ),
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='profile_img/anonymous.png', upload_to='profile_img/'),
        ),
    ]
