#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django import forms
from django.forms import ModelForm
from django.contrib.auth import authenticate
from django.contrib.auth.models import User as django_User
from .models import User as MyUser, Admin, StoreManager, PromotionManager

class LoginForm(ModelForm):
    class Meta:
        model = django_User
        fields = ['email', 'password']

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if not django_User.objects.filter(email=email).exists():
            raise forms.ValidationError("Your email address is not registered!")

        return email

class DjangoUserForm(ModelForm):
    class Meta:
        model = django_User
        fields = ['username', 'password']

    def __init__(self, *args, **kwargs):
        super(DjangoUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'placeholder': 'Username', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})

    def clean_username(self):
        username = self.cleaned_data.get('username')
        
        if django_User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username already exists!")

        return username

class DjangoUserEditForm(ModelForm):
    new_password = forms.CharField(label='New password')

    class Meta:
        model = django_User
        fields = ['first_name', 'last_name', 'password']

    def __init__(self, *args, **kwargs):
        super(DjangoUserEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder': 'Name', 'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'Last Name', 'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['new_password'].widget.attrs.update({'placeholder': 'Password', 'class': 'form-control'})
        self.fields['password'].required = False
        self.fields['new_password'].required = False

    def clean(self):
        password = self.cleaned_data.get('password')
        new_password = self.cleaned_data.get('new_password')

        if password == new_password:
            return self.cleaned_data
        raise forms.ValidationError("The passwords don't match!")

class StoreManagerForm(ModelForm):
    class Meta:
        model = StoreManager
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(StoreManagerForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if StoreManager.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered!")

        return email

class PromotionManagerForm(ModelForm):
    class Meta:
        model = PromotionManager
        fields = ['email']

    def __init__(self, *args, **kwargs):
        super(PromotionManagerForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'placeholder': 'Email', 'class': 'form-control'})

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if PromotionManager.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered!")

        return email