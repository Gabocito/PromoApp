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
    email = models.EmailField(max_length=70, unique=True, blank=True)

    def __unicode__(self):
        return self.user.username + ' ' + self.acc_type
 
class StoreManager(models.Model):
    user = models.OneToOneField(django_User)
    user_type = models.CharField(max_length=200, default='Store Manager')
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=70, unique=True, blank=True)
    stores = models.ManyToManyField('promoapp_business.Store')

    def __unicode__(self):
        return self.user.username

class PromotionManager(models.Model):
    user = models.OneToOneField(django_User)
    user_type = models.CharField(max_length=200, default='Promotion Manager')
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=70, unique=True, blank=True)

    def __unicode__(self):
        return self.user.username
 
class Admin(models.Model):
    user = models.OneToOneField(django_User)
    user_type = models.CharField(max_length=200, default='Admin')
    email = models.EmailField(max_length=70, unique=True, blank=True)

    def __unicode__(self):
        return self.user.username