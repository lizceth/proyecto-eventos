from django.contrib import admin
from eventos.models import *
from django.contrib.auth.models import User


class PonenteAdmin(admin.ModelAdmin):
    list_display =['tema_ponencia']
    list_filter =['persona']

class Area_organizadoraAdmin(admin.ModelAdmin):
    list_filter=['integrantes','comision','otros']

class TallerInline(admin.StackedInline):
    model=Taller
    extra=3

class EventoAdmin(admin.ModelAdmin):
    list_display = ['nombre','fecha_inicio','fecha_final','tipo_evento','descripcion','costo','monto']
    list_filter = ['ponente','area_organizadora','participantes','imagen']

    inlines=[TallerInline]

class Ponente_eventoAdmin(admin.ModelAdmin):
    list_display=['inicio', 'final',]
    list_filter=['evento','ponente']


admin.site.register(Ponente, PonenteAdmin)
admin.site.register(Area_organizadora, Area_organizadoraAdmin)
admin.site.register(Evento, EventoAdmin)
admin.site.register(Ponente_evento,Ponente_eventoAdmin)

