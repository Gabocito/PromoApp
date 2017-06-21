#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class PromotionForm(forms.Form):
    description = forms.CharField(label='Descripción', max_length=200)
    discount = forms.IntegerField(label='Descuento', min_value=1, max_value=100)
    products = forms.CharField(label='Productos', max_length=200)

class PromotionEditForm(forms.Form):
    description = forms.CharField(label='Descripción', max_length=200)
    discount = forms.IntegerField(label='Descuento', min_value=1, max_value=100)
    products = forms.CharField(label='Productos', max_length=200)

class AdvertisingCampaignForm(forms.Form):
    target = forms.CharField(label='Target' ,max_length=32)
    start_date = forms.DateField(label='Fecha de Inicio', widget=DateInput())
    end_date = forms.DateField(label='Fecha de Fin', widget=DateInput())

class AdvertisingCampaignEditForm(forms.Form):
    target = forms.CharField(label='Target' ,max_length=32)
    start_date = forms.DateField(label='Fecha de Inicio', widget=DateInput())
    end_date = forms.DateField(label='Fecha de Fin', widget=DateInput())

class CompanyForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=32)
    rif = forms.CharField(label='Rif', max_length=32)
    commercial_sector = forms.CharField(label='Sector Comercial', max_length=32)
    address = forms.CharField(label='Dirección', max_length=200)
    email = forms.EmailField()

class CompanyEditForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=32)
    rif = forms.CharField(label='Rif', max_length=32)
    commercial_sector = forms.CharField(label='Sector Comercial', max_length=32)
    address = forms.CharField(label='Dirección', max_length=200)
    email = forms.EmailField()

class StoreForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=32)
    rif = forms.CharField(label='Rif', max_length=32)
    address = forms.CharField(label='Dirección', max_length=200)
    email = forms.EmailField()

class StoreEditForm(forms.Form):
    name = forms.CharField(label='Nombre', max_length=32)
    rif = forms.CharField(label='Rif', max_length=32)
    address = forms.CharField(label='Dirección', max_length=200)
    email = forms.EmailField()