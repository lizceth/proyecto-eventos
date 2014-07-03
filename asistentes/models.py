# coding: utf-8
#from eventos.models import Evento
from django.db import models

# Create your models here.

ACADEMICO=(
    ('PROFESIONAL','Profesional'),
    ('ESTUDIANTE','Estudiante'),
    ('OTROS','Otros'),
)
class Persona(models.Model):
    dni=models.IntegerField(max_length=8)
    nombre= models.CharField(max_length=30)
    apellido_pat=models.CharField(max_length=30)
    apellido_mat= models.CharField(max_length=30)
    grado_academico=models.CharField(max_length=11, choices=ACADEMICO, default='0')
    def __unicode__(self):
        return '%s  %s' %(self.nombre, self.apellido_pat)

PARTICIPANTE=(
    ('PONENTE','Ponente'),
    ('ASISTENTE','Asistente'),
)
class Participante(models.Model):
    tipo_participante = models.CharField(max_length=9, choices=PARTICIPANTE)
    persona = models.ForeignKey(Persona)
    #evento = models.ForeignKey(Evento)
    def __unicode__(self):
        return self.persona.nombre




