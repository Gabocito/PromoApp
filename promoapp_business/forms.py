#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

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
    