from django.contrib import admin
from academicos.models import Coordinador, Escuela, Facultad
from django.contrib.auth.models import User
# Register your models here.

class EscuelaInline(admin.TabularInline):
    model = Escuela
    extra=1

class CoordinadorAdmin(admin.ModelAdmin):
    fieldsets = [
        ('None', {'fields' : ['tipo_coordinador']}),
        ('None', {'fields' : ['nombre']}),
    ]
    list_filter=['nombre']
    inlines = [EscuelaInline]

class FacultadAdmin(admin.ModelAdmin):
    list_display=['nombre']
    list_filter=['coordinador_fac']


admin.site.register(Coordinador, CoordinadorAdmin)
admin.site.register(Facultad, FacultadAdmin)

