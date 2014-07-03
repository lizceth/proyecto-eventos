# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from asistentes.models import *
from academicos.models import *
from django.utils import timezone
from datetime import *

class Ponente(models.Model):
    tema_ponencia = models.CharField(max_length=50)
    persona = models.ForeignKey(Persona)
    def __unicode__(self):
        return '%s %s -->%s' %(self.persona.nombre, self.persona.apellido_pat, self.tema_ponencia)

class Area_organizadora(models.Model):
    integrantes=models.ForeignKey(Persona)
    comision=models.ForeignKey(Escuela, null=True)
    otros=models.CharField(max_length=40, null=True)
    def __unicode__(self):
        return "%s %s "%(self.comision.nombre, self.otros)

tipo_evento=(
    ('Simposio','Simposio'),
    ('Congreso', 'congreso'),
    ('Jornada', 'Jornada'),
    ('Cientifico','Cientifico'),
    ('Seminario', 'Seminario'),
    ('Panel','Panel'),
    ('Cursos', 'Cursos'),
    ('Feria y Exposicion','Feria y Exposicion'),
    ('Musica','Musica'),
    ('Social','Social'),
    ('Espiritual', 'Espiritual'),
    )

COSTO= (('Precio','Precio'),
        ('Gratuito','Gratuito'),
)
ACTIVIDAD=(
    ('T','Taller'),
    ('C','Charla'),
    ('O','Otro'),
)
PARTICIPANTE=(
    ('Ponente', 'Ponente'),
    ('Asistente', 'Asistente'),)

class Evento(models.Model):
    nombre = models.CharField(max_length=102)
    ponente=models.ManyToManyField(Ponente)
    fecha_inicio = models.DateTimeField()
    fecha_final = models.DateTimeField()
    area_organizadora = models.ForeignKey(Area_organizadora)
    tipo_evento = models.CharField(max_length=18, choices=tipo_evento, default='0')
    participantes=models.ManyToManyField(Participante)
    imagen=models.ImageField(upload_to= 'imagen', verbose_name='imagen')
    descripcion=models.TextField()
    costo=models.CharField(max_length=8, choices=COSTO, default='G')
    monto=models.FloatField( default=0.00 )
    def __unicode__(self):
        return '%s -- %s' %(self.nombre, self.tipo_evento)
"""
    def ultimos_eventos(self):
        mes=timezone.now().month
        reciente=Evento.objects.get(fecha_inicio__month=mes)
        return reciente

    def evento(self):
        return self.nombre

    def ponente(self):
        return self.ponente.nombre

    def tipo_evento(self):
        return self.tipo_evento

    def area_organizadora(self):
        return self.area_organizadora.comision
"""



class Taller(models.Model):
    tema = models.CharField(max_length=50)
    actividad = models.CharField(max_length=1, choices=ACTIVIDAD, default='O')
    evento=models.ForeignKey(Evento)
    def __unicode__(self):
        return '%s: %s--> %s' %(self.actividad, self.tema)

class Ponente_evento(models.Model):
    inicio = models.DateTimeField()
    final = models.DateTimeField()
    evento = models.ForeignKey(Evento)
    ponente = models.ForeignKey(Ponente)
    def __unicode__(self):
        return self.ponente.tema_ponencia


