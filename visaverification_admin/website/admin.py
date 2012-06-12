from django.contrib import admin
from website.models import Site
from website.models import User
from website.models import CorporateEmail
from django import forms
from django.forms import ModelForm, PasswordInput


class CorporateEmailForm(forms.ModelForm):
    password = forms.CharField(widget=PasswordInput())


class CorporateEmailAdmin(admin.ModelAdmin):
    form = CorporateEmailForm

admin.site.register(Site)
admin.site.register(User)
admin.site.register(CorporateEmail, CorporateEmailAdmin)

