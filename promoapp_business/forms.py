#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

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
    start_date = forms.DateTimeField(label='Fecha de Inicio')
    end_date = forms.DateTimeField(label='Fecha de Finalización')

class AdvertisingCampaignEditForm(forms.Form):
    target = forms.CharField(label='Target' ,max_length=32)
    start_date = forms.DateTimeField(label='Fecha de Inicio')
    end_date = forms.DateTimeField(label='Fecha de Finalización')

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