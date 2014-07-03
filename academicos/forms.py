# coding:utf-8
from django.forms import ModelForm
from django import forms
from academicos.models import Coordinador, Escuela, Facultad

class CoordinadorForm(ModelForm):
    class Meta:
        model = Coordinador

class EscuelaForm(ModelForm):
    class Meta:
        model = Escuela

class FacultadForm(ModelForm):
    class Meta:
        model = Facultad




