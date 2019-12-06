from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.validators import FileExtensionValidator

from django import forms

class MyForm(forms.Form):
    field = forms.FileField(label='Upload video', validators=[FileExtensionValidator(allowed_extensions=["mp4", "avi", "flv"])])