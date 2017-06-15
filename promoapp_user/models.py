#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User as django_User
 
class User(models.Model):
    user = models.OneToOneField(django_User)
    user_type = models.CharField(max_length=200, default='User')
    CHOICES = (
        ('FB', 'Facebook'),
        ('G', 'Google'),
        ('TW', 'Twitter'),
    )
    acc_type = models.CharField(max_length=200, choices=CHOICES, default='FB')
    promotions = models.ManyToManyField('promoapp_business.Promotion')

    def __unicode__(self):
        return self.user_type + ' ' + self.user.username + ' ' + self.acc_type
 
class StoreManager(models.Model):
    user = models.OneToOneField(django_User)
    user_type = models.CharField(max_length=200, default='Store Manager')
    is_active = models.BooleanField()
    stores = models.ManyToManyField('promoapp_business.Store')
    # acc_id = models.CharField(max_length=200, default='0')
    # acc_type = models.CharField(max_length=200, default='none')

    def __unicode__(self):
        return self.user_type + ' ' + self.user.username

class PromotionManager(models.Model):
    user = models.OneToOneField(django_User)
    user_type = models.CharField(max_length=200, default='Promotion Manager')
    is_active = models.BooleanField()
    promotions = models.ManyToManyField('promoapp_business.Promotion')
    # acc_type = models.CharField(max_length=200, default='none')
    # company_name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.user_type + ' ' + self.user.username
 
class Admin(models.Model):
    user = models.OneToOneField(django_User)
    user_type = models.CharField(max_length=200, default='Admin')

    def __unicode__(self):
        return self.user_type + ' ' + self.user.username