#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms

class StoreManagerForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField()
    password = forms.CharField(label='Contraseña', max_length=30, widget=forms.PasswordInput)

class StoreManagerEditForm(forms.Form):
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellido', max_length=30)
    password = forms.CharField(label='Contraseña', max_length=30, widget=forms.PasswordInput)

class PromotionManagerForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField()
    password = forms.CharField(label='Contraseña', max_length=30, widget=forms.PasswordInput)

class PromotionManagerEditForm(forms.Form):
    first_name = forms.CharField(label='Nombre', max_length=30)
    last_name = forms.CharField(label='Apellido', max_length=30)
    password = forms.CharField(label='Contraseña', max_length=30, widget=forms.PasswordInput)