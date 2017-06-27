#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.forms import ModelForm
from models import *

class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'rif', 'commercial_sector', 'address', 'email']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name', 'class': 'form-control'})
        self.fields['rif'].widget.attrs.update({'placeholder': 'Rif', 'class': 'form-control'})
        self.fields['commercial_sector'].widget.attrs.update({'placeholder': 'Area', 'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Address', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})

class CompanyEditForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'rif', 'commercial_sector', 'address', 'email']

    def __init__(self, *args, **kwargs):
        super(CompanyForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name', 'class': 'form-control'})
        self.fields['rif'].widget.attrs.update({'placeholder': 'Rif', 'class': 'form-control'})
        self.fields['commercial_sector'].widget.attrs.update({'placeholder': 'Area', 'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Address', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})

class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'rif', 'address', 'email']

    def __init__(self, *args, **kwargs):
        super(StoreForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name', 'class': 'form-control'})
        self.fields['rif'].widget.attrs.update({'placeholder': 'Rif', 'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Address', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})

class StoreEditForm(ModelForm):
    class Meta:
        model = Store
        fields = ['name', 'rif', 'address', 'email', 'advertisingcampaigns']

    def __init__(self, *args, **kwargs):
        super(StoreEditForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'placeholder': 'Name', 'class': 'form-control'})
        self.fields['rif'].widget.attrs.update({'placeholder': 'Rif', 'class': 'form-control'})
        self.fields['address'].widget.attrs.update({'placeholder': 'Address', 'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})
        self.fields['advertisingcampaigns'].widget.attrs.update({'class': 'selectpicker'})