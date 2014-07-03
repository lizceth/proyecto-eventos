# coding:utf-8
from django.forms import ModelForm
from django import forms
from aplicacion_evento.models import Persona, Ponente, Coordinador, Escuela, Facultad, Area_organizadora,  Evento, Participante, Taller_seminario, Ponente_evento, Asistentes

class UsuarioForm(forms.Form):
    correo = forms.EmailField(label='Tu correo Electronico')
    mensaje = forms.CharField(widget=forms.Textarea)



