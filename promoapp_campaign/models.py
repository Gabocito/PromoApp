from __future__ import unicode_literals

from django.db import models

from django.core.validators import MaxValueValidator, MinValueValidator

class Promotion(models.Model):
    description = models.CharField(max_length=200,default='')
    discount = models.IntegerField(
        default = 1,
        validators = [MaxValueValidator(100), MinValueValidator(1)]
    )
    products = models.CharField(max_length=200,default='')
    is_active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.description

class AdvertisingCampaign(models.Model):
    target = models.CharField(max_length=32)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    promotions = models.ManyToManyField(Promotion)

    def __unicode__(self):
        return self.target