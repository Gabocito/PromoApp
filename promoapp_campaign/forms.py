#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import *

class PromotionForm(ModelForm):
    class Meta:
        model = Promotion
        fields = ['description', 'discount', 'products']

    def __init__(self, *args, **kwargs):
        super(PromotionForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'placeholder': 'Description', 'class': 'form-control'})
        self.fields['discount'].widget.attrs.update({'placeholder': 'Discount', 'class': 'form-control'})
        self.fields['products'].widget.attrs.update({'placeholder': 'Products', 'class': 'form-control'})

class PromotionEditForm(ModelForm):
    class Meta:
        model = Promotion
        fields = ['description', 'discount', 'products']

    def __init__(self, *args, **kwargs):
        super(PromotionEditForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({'placeholder': 'Description', 'class': 'form-control'})
        self.fields['discount'].widget.attrs.update({'placeholder': 'Discount', 'class': 'form-control'})
        self.fields['products'].widget.attrs.update({'placeholder': 'Products', 'class': 'form-control'})

class AdvertisingCampaignForm(ModelForm):
    class Meta:
        model = AdvertisingCampaign
        fields = ['target', 'start_date', 'end_date']

    def __init__(self, *args, **kwargs):
        super(AdvertisingCampaignForm, self).__init__(*args, **kwargs)
        self.fields['target'].widget.attrs.update({'placeholder': 'Target', 'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'placeholder': 'Start Date', 'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'placeholder': 'End Date', 'class': 'form-control'})

class AdvertisingCampaignEditForm(ModelForm):
    class Meta:
        model = AdvertisingCampaign
        fields = ['target', 'start_date', 'end_date', 'promotions']

    def __init__(self, *args, **kwargs):
        super(AdvertisingCampaignEditForm, self).__init__(*args, **kwargs)
        self.fields['target'].widget.attrs.update({'placeholder': 'Target', 'class': 'form-control'})
        self.fields['start_date'].widget.attrs.update({'placeholder': 'Start Date', 'class': 'form-control'})
        self.fields['end_date'].widget.attrs.update({'placeholder': 'End Date', 'class': 'form-control'})
        self.fields['promotions'].widget.attrs.update({'class': 'form-control select2', 'data-placeholder': "Select a promotion", 'style': 'width: 100%;'})