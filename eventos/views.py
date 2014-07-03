from django.shortcuts import render, render_to_response, get_object_or_404
from eventos.models import  Ponente, Area_organizadora,  Evento, Taller, Ponente_evento
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from eventos.forms import PonenteForm, Area_organizadoraForm, EventoForm, TallerForm, Ponente_eventoForm
from django.utils import timezone
#from django.db.models import Q
#from django.core.paginator import Paginator, InvalidPage, emptyPage
"""
def buscar_eventos(request):
    buscar=request.GET.get('q', '')
    buscar1=request.GET.get('c', '')

    evento=Ponente.objects.all()

    resultado=Evento.objects.all()
    if buscar1:
        resultado1=resultado.filter(Ponente__id=buscar1)
    else:
        resultado1=resultado
    if buscar:
        qset=(
            Q(evento__icontains=buscar)|
            Q(ponente__icontains=buscar)|
            Q(tipo_evento__=buscar)|
            Q(area_organizadora__icontains=buscar)|
        )





    return render_to_response('eventos/inicio.html', {'ultimos':ultimos},
context_instance=RequestContext(request))
"""
def inicio(request):
    eventos = Evento.objects.order_by('fecha_inicio')
    return render_to_response('base_principal.html',{'eventos':eventos},
                              context_instance=RequestContext(request))
def detalle(request, id_evento):
    evento = get_object_or_404(Evento, id=id_evento)
    return render(request, 'eventos/detalle.html',
                  {'evento':evento})


def sobre(request):
    titulo = 'pagina de eventos academicos'
    return render_to_response('eventos/sobre.html',{'titulo':titulo},
                              context_instance=RequestContext(request))

def Ponentes(request):
    ponentes = Ponente.objects.all()
    titulo = "pagina  de  ponentes "
    return render_to_response('eventos/ponente.html', {
        'ponentes':ponentes,'titulo':titulo},
         context_instance=RequestContext(request))

def ponente_add(request):
    if request.method == 'POST':
        formulario = PonenteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/ponenteList/')
    else:
        formulario = PonenteForm()
    return render_to_response('eventos/ponenteform.html',
                              {'formulario':formulario},
                          context_instance=RequestContext(request))


def Ponente_edit (request, id):
        ponente_edit= Ponente.objects.get(pk=id)
        if request.method == 'POST':
            formulario = PonenteForm(request.POST, instance = ponente_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/ponenteList/")
        else:
            formulario = PonenteForm(instance= ponente_edit)
        return render_to_response('eventos/ponenteEdit.html',
                                 {'formulario': formulario},
                                  context_instance = RequestContext(request))
def Ponente_borrar (request, id):
    ponente_borrar = get_object_or_404(Ponente, pk=id)
    ponente_borrar.delete()
    return HttpResponseRedirect("/ponenteList/")

def Area_organizadoras(request):
    area_organizadora = Area_organizadora.objects.all()
    titulo = "Lista a las  Areas que Organizan"
    return render_to_response('eventos/area_organizadora.html',{
             'area_organizadora':area_organizadora,'titulo':titulo},
             context_instance=RequestContext(request))

def Area_org_add(request):
    if request.method == "POST":
        formulario = Area_organizadoraForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/area_organizadoraList/')
    else:
        formulario = Area_organizadoraForm()
    return render_to_response('eventos/area_organizadoraAdd.html',
                              {'formulario': formulario},
                               context_instance = RequestContext(request))

def Area_org_edit (request, id):
        area_org_edit= Area_organizadora.objects.get(pk=id)
        if request.method == 'POST':
            formulario = Area_organizadoraForm(request.POST, instance = area_org_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/area_organizadoraList/")
        else:
            formulario = Area_organizadoraForm(instance= area_org_edit)
        return render_to_response('eventos/area_organizadoraEdit.html',
                                 {'formulario': formulario},
                                  context_instance = RequestContext(request))
def Area_org_borrar (request, id):
    area_org_borrar = get_object_or_404(Area_organizadora, pk=id)
    area_org_borrar.delete()
    return HttpResponseRedirect("/area_organizadoraList/")

def Eventos(request):
    eventos = Evento.objects.all()
    titulo = "Pagina de Eventos Registrados "
    return render_to_response('eventos/evento.html',{
                               'eventos':eventos,'titulo':titulo},
                               context_instance=RequestContext(request))
def EventosComp(request):
    eventos = Evento.objects.all()
    titulo = "Pagina de Eventos Registrados "
    return render_to_response('eventos/eventoComp.html',{
                               'eventos':eventos,'titulo':titulo},
                               context_instance=RequestContext(request))
def Eventos_add(request):
    if request.method == "POST":
        formulario = EventoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/eventosList/')
    else:
        formulario = EventoForm()
    return render_to_response('eventos/eventoAdd.html',
                             {'formulario': formulario},
                              context_instance = RequestContext(request))

def Eventos_edit (request, id):
    evento_edit= Evento.objects.get(pk=id)
    if request.method == 'POST':
        formulario = EventoForm(request.POST, instance = evento_edit)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/eventosList/")
    else:
        formulario = EventoForm(instance= evento_edit)
    return render_to_response('eventos/eventoEdit.html',
                              {'formulario': formulario},
                               context_instance = RequestContext(request))
def Evento_borrar (request, id):
    evento_borrar = get_object_or_404(Evento, pk=id)
    evento_borrar.delete()
    return HttpResponseRedirect("/eventosList/")


def taller(request):
    taller = Taller.objects.all()
    titulo = "Talleres o Seminarios Registrados"
    return render_to_response('eventos/taller.html',{
                              'taller':taller,'titulo':titulo},
                               context_instance=RequestContext(request))

def taller_add(request):
     if request.method == "POST":
         formulario = TallerForm(request.POST)
         if formulario.is_valid():
             formulario.save()
             return HttpResponseRedirect('/taller_list/')
     else:
         formulario = TallerForm()
     return render_to_response('eventos/tallerAdd.html',
                                 {'formulario': formulario},
                                  context_instance = RequestContext(request))

def taller_edit (request, id):
    taller_edit=Taller.objects.get(pk=id)
    if request.method == 'POST':
        formulario = TallerForm(request.POST, instance = tall_sem_edit)
        if formulario.is_valid():
            formualrio.save()
            return HttpResponceRedirect("/taller_list/")
        else:
            formulario=TallerForm(instance=tall_sem_edit)
        return render_to_response('eventos/tallerEdit.html',
                                  {'formulario':formualrio},
                                  context_instance=RequestContext(request))

def taller_borrar (request, id):
    taller_borrar=get_object_or_404(Taller, pk=id)
    taller_borrar.delete()
    return HttpResponseRedirect("/taller_list/")

def Ponente_eventos(request):
    ponente_eventos = Ponente_evento.objects.all()
    titulo = "Ponentes de los Eventos "
    return render_to_response('eventos/ponente_eventoList.html',{
                              'ponente_eventos':ponente_eventos,'titulo':titulo},
                               context_instance=RequestContext(request))

def pon_eve_add(request):
    if request.method == 'post':
        formulario = Ponente_eventoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/ponente_eventoList/')
    else:
        formulario = Ponente_eventoForm()
    return render_to_response('eventos/ponente_eventoAdd.html',
                          {'formulario':formulario},
                          context_instance=RequestContext(request))

def pon_eve_edit (request,id):
    pon_eve_edit=Ponente_evento.objects.get(pk=id)
    if request.method == 'POST':
        formulario = Ponente_eventoForm(request.POST, instance=pon_eve_edit)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect("/ponente_eventoList/")
        else:
            formulario = Ponente_eventoForm(instance=pon_eve_edit)
        return render_to_response('eventos/ponente_eventoEdit.html',
                                  {'formulario':formulario},
                                  context_instance = RequestContext(request))

def Pon_Eve_borrar (request, id):
    pon_eve_borrar = get_object_or_404(Ponente_evento, pk=id)
    pon_eve_borrar.delete()
    return HttpResponseRedirect('/ponente_eventoList/')
