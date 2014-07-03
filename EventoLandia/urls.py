from django.conf.urls.static import static
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', 'eventoLandia.views.inicio'),
    url(r'^$','eventos.views.inicio', name='inicio'),
    url(r'^sobre/$','eventos.views.sobre'),
   # url(r'^$','eventos.views.ultimos_eventos'),

    #aplicacion asistentes
    url(r'^personaList/$','asistentes.views.Personas'),
    url(r'^personaAdd/$','asistentes.views.persona_add'),
    url(r'^personaEdit/(?P<id>\d+)$','asistentes.views.Persona_edit'),
    url(r'^personaBorrar/(?P<id>\d+)$','asistentes.views.Persona_borrar'),
    url(r'^participantesList/$','asistentes.views.Participantes'),
    url(r'^participantesAdd/$','asistentes.views.Participantes_add'),
    url(r'^participantesEdit/(?P<id>\d+)$','asistentes.views.Participantes_edit'),
    url(r'^participantesBorrar/(?P<id>\d+)$','asistentes.views.Participantes_borrar'),

    # aplicacion academicos
    url(r'^cordinadoresList/$','academicos.views.Cordinadores'),
    url(r'^cordinadoresAdd/$','academicos.views.Cordinador_add'),
    url(r'^cordinadorEdit/(?P<id>\d+)$','academicos.views.Cordinador_edit'),
    url(r'^cordinadorBorrar/(?P<id>\d+)$','academicos.views.Cordinador_borrar'),
    url(r'^escuelaList/$','academicos.views.Escuelas'),
    url(r'^escuelaAdd/','academicos.views.Escuela_add'),
    url(r'^escuelaEdit/(?P<id>\d+)$','academicos.views.Escuela_edit'),
    url(r'^escuelaBorrar/(?P<id>\d+)$','academicos.views.Escuelas_borrar'),
    url(r'^facultadesList/$','academicos.views.Facultades'),
    url(r'^facultadesAdd/$','academicos.views.Facultad_add'),
    url(r'^facultadesEdit/(?P<id>\d+)$','academicos.views.Facultad_edit'),
    url(r'^facultadesBorrar/(?P<id>\d+)$','academicos.views.Facultad_borrar'),

    #aplicacion eventos
    url(r'^detalle/(?P<id_evento>\d+)$','eventos.views.detalle'),
    url(r'^eventos/$','eventos.views.inicio'),
    url(r'^ponenteList/$','eventos.views.Ponentes'),
    url(r'^ponenteAdd/$','eventos.views.ponente_add'),
    url(r'^ponenteEdit/(?P<id>\d+)$','eventos.views.Ponente_edit'),
    url(r'^ponenteBorrar/(?P<id>\d+)$','eventos.views.Ponente_borrar'),
    url(r'^area_organizadoraList/$','eventos.views.Area_organizadoras'),
    url(r'^area_organizadoraAdd/$','eventos.views.Area_org_add'),
    url(r'^area_organizadoraEdit/(?P<id>\d+)$','eventos.views.Area_org_edit'),
    url(r'^area_organizadoraBorrar/(?P<id>\d+)$','eventos.views.Area_org_borrar'),
    url(r'^eventosList/$','eventos.views.Eventos'),
    url(r'^eventosListComp/$','eventos.views.EventosComp'),
    url(r'^eventosAdd/$','eventos.views.Eventos_add'),
    url(r'^eventosEdit/(?P<id>\d+)$','eventos.views.Eventos_edit'),
    url(r'^eventosBorrar/(?P<id>\d+)$','eventos.views.Evento_borrar'),
    url(r'^taller_list/$','eventos.views.taller'),
    url(r'^taller_add/$','eventos.views.taller_add'),
    url(r'^taller_edit/(?P<id>\d+)$','eventos.views.taller_edit'),
    url(r'^taller_borrar/(?P<id>\d+)$','eventos.views.taller_borrar'),
    url(r'^ponente_eventoList/$','eventos.views.Ponente_eventos'),
    url(r'^ponente_eventoAdd/$','eventos.views.pon_eve_add'),
    url(r'^ponente_eventoEdit/(?P<id>\d+)$','eventos.views.pon_eve_edit'),
    url(r'^ponente_eventoBorrar/(?P<id>\d+)$','eventos.views.Pon_Eve_borrar'),

    # aplicacion usuario
    url(r'^ingresar/$','usuarios.views.ingresar'),
    url(r'^privado/$','usuarios.views.privado'),
    url(r'^sesion/$','usuarios.views.index'),
    url(r'^cerrar/$','usuarios.views.cerrar'),
    url(r'^usuarios/$','usuarios.views.usuario'),
    url(r'^usuario/nuevo/$','usuarios.views.nuevo'),
    url(r'^editar/(?P<id>\d+)$','usuarios.views.editar'),
    url(r'^borrar/(?P<id>\d+)$','usuarios.views.borrar'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




