# coding:utf-8
from django.forms import ModelForm
from django import forms
from asistentes.models import Persona, Participante

class PersonaForm(ModelForm):
    class Meta:
        model = Persona

class ParticipanteForm(ModelForm):
    class Meta:
        model = Participante


