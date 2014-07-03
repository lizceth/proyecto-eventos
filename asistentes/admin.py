from django.contrib import admin
from asistentes.models import Persona, Participante
from django.contrib.auth.models import User
# Register your models here.

class ParticipanteInline(admin.TabularInline):
    model=Participante
    extra=1

class PersonaAdmin(admin.ModelAdmin):
    fieldsets=[
        (None,               {'fields':['dni']}),
        (None,   {'fields':['nombre']}),
        (None,   {'fields':['apellido_pat']}),
        (None,     {'fields':['apellido_mat']}),
        (None,     {'fields':['grado_academico']}),
    ]
    inlines=[ParticipanteInline]



admin.site.register(Persona, PersonaAdmin)
admin.site.register(Participante)



