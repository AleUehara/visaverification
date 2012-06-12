#-*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, PasswordInput

class EmailForm(ModelForm):
    password = forms.CharField(widget=PasswordInput())
    class Meta:
        model = Email