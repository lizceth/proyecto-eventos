# coding:utf-8
from django.forms import ModelForm
from django import forms
from eventos.models import Ponente, Area_organizadora, Evento, Taller, Ponente_evento

class PonenteForm(ModelForm):
     class Meta:
         model = Ponente

class Area_organizadoraForm(ModelForm):
     class Meta:
         model = Area_organizadora

class EventoForm(ModelForm):
     class Meta:
         model = Evento


class TallerForm(ModelForm):
     class Meta:
         model = Taller

class Ponente_eventoForm(ModelForm):
     class Meta:
         model = Ponente_evento

