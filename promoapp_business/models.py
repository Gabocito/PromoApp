from __future__ import unicode_literals

from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=32)
    rif = models.CharField(max_length=32)
    commercial_sector = models.CharField(max_length=32)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name + ' rif:' + self.rif

class Store(models.Model):
    name = models.CharField(max_length=32)
    rif = models.CharField(max_length=32)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)
    is_active = models.BooleanField(default=True)
    advertisingcampaigns = models.ManyToManyField('promoapp_campaign.AdvertisingCampaign')

    def __unicode__(self):
        return self.name + ' rif:' + self.rif