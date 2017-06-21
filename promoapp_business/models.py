from __future__ import unicode_literals

from django.core.validators import MaxValueValidator, MinValueValidator

from django.db import models

class Promotion(models.Model):
    description = models.CharField(max_length=200,default='')
    discount = models.IntegerField(
        default = 1,
        validators = [MaxValueValidator(100), MinValueValidator(1)]
    )
    products = models.CharField(max_length=200,default='')

    def __unicode__(self):
        return self.description

class AdvertisingCampaign(models.Model):
    target = models.CharField(max_length=32)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.target

class CompanyAdvertisingCampaign(models.Model):
    company = models.ForeignKey('Company')
    advertisingcampaign = models.ForeignKey(AdvertisingCampaign)

    promotion = models.ForeignKey(Promotion)

class Company(models.Model):
    name = models.CharField(max_length=32)
    rif = models.CharField(max_length=32)
    commercial_sector = models.CharField(max_length=32,default='Todos')
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)
    is_active = models.BooleanField()
    advertisingcampaigns = models.ManyToManyField(AdvertisingCampaign, through=CompanyAdvertisingCampaign)

    def __unicode__(self):
        return self.name + ' rif:' + self.rif

class Store(models.Model):
    name = models.CharField(max_length=32)
    rif = models.CharField(max_length=32)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=70,blank=True)

    def __unicode__(self):
        return self.name + ' rif:' + self.rif