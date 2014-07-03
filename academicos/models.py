# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from asistentes.models import Persona

# Create your models here.

TIPO=(
    ('ESCUELA','Escuela'),
    ('FACULTAD', 'Facultad'),)

class Coordinador(models.Model):
    nombre=models.ForeignKey(Persona)
    tipo_coordinador=models.CharField(max_length=8 ,choices=TIPO)
    def __unicode__(self):
        return '%s %s -%s' %(self.nombre.nombre, self.nombre.apellido_pat,self.tipo_coordinador)

ESCUELA=(
    ('Sistemas','Ingenieria de Sistemas'),
    ('Civil','Ingenieria Civil'),
    ('Ambiental','Ingenieria Ambiental'),
    ('Alimentos','Ingenieria de Alimentos'),
    ('Contabilidad','Contabilidad y Gestion Tributaria'),
    ('Administracion','Administracion y Negocios Internacionales'),
    ('Asistencia Gerencial','Asistencia Gerencial'),
    ('Psicologia','Psicologia'),
    ('Enfermeria','Enfermeria'),
    ('Ed.Inicicial','Educacion Inicial y Puericultura'),
    ('Ed.Bililingue','Educacion Intercultural Bilingue'),
    ('Ed.Linguistica','Educacion Linguistica e Ingles'),
    ('Ed.primaria','Educacion Primaria'),)

class Escuela(models.Model):
    nombre = models.CharField(max_length=20, choices=ESCUELA)
    coordinador_esc = models.ForeignKey(Coordinador)
    def __unicode__(self):
        return self.nombre

FAC=(('FIA','Ingenieria y arquitectura'),
     ('CIEMPRE','Ciencias Empresariales'),
     ('SALUD','salud'),
     ('FACIHED','ciencias humanas y Educacion'),)

class Facultad(models.Model):
    nombre = models.CharField(max_length=7, choices=FAC)
    coordinador_fac = models.ForeignKey(Coordinador)
    escuela = models.ForeignKey(Escuela, null=True)
    def __unicode__(self):
        return self.nombre

