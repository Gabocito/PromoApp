from django import forms

class StoreManagerForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)

class PromotionManagerForm(forms.Form):
    username = forms.CharField(label='Usuario', max_length=30)
    email = forms.EmailField()
    password = forms.CharField(label='Password', max_length=30, widget=forms.PasswordInput)

