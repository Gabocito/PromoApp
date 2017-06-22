#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class PromotionForm(forms.Form):
    description = forms.CharField(label='Description', max_length=200)
    discount = forms.IntegerField(label='Discount', min_value=1, max_value=100)
    products = forms.CharField(label='Products', max_length=200)

class PromotionEditForm(forms.Form):
    description = forms.CharField(label='Description', max_length=200)
    discount = forms.IntegerField(label='Discount', min_value=1, max_value=100)
    products = forms.CharField(label='Products', max_length=200)

class AdvertisingCampaignForm(forms.Form):
    target = forms.CharField(label='Target' ,max_length=32)
    start_date = forms.DateField(label='Start Date', widget=DateInput())
    end_date = forms.DateField(label='End Date', widget=DateInput())

class AdvertisingCampaignEditForm(forms.Form):
    target = forms.CharField(label='Target' ,max_length=32)
    start_date = forms.DateField(label='Start Date', widget=DateInput())
    end_date = forms.DateField(label='End Date', widget=DateInput())
    