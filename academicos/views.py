from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, get_object_or_404
from academicos.models import Coordinador, Escuela, Facultad
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from asistentes.models import Persona
from asistentes.forms import *
#from django.core.mail import EmailMessage
#from django.contrib.auth.forms import UserCreationForm, AuthentificationForm
#from django.contrib.auth import login, authentificate, logout
#from django.contrib.auth.decorators import login_required
from academicos.forms import CoordinadorForm, EscuelaForm, FacultadForm

def Cordinadores(request):
    cordinadores = Coordinador.objects.all()
    titulo = "Lista de Cordinadores"
    return render_to_response('academicos/cordinadoresList.html',{
                      'cordinadores':cordinadores,'titulo':titulo},
                         context_instance=RequestContext(request))

def Cordinador_add(request):
    if request.method == "POST":
        formulario = CoordinadorForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/cordinadoresList/')
    else:
        formulario = CoordinadorForm()
    return render_to_response('academicos/cordinadoresAdd.html',
                             {'formulario': formulario},
                     context_instance = RequestContext(request))

def Cordinador_edit (request, id):
        cordinador_edit= Coordinador.objects.get(pk=id)
        if request.method == 'POST':
            formulario = CoordinadorForm(
                request.POST, instance = cordinador_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/cordinadoresList/")
        else:
            formulario = CoordinadorForm(instance= cordinador_edit)
        return render_to_response('academicos/cordinadoresEdit.html',
                                 {'formulario': formulario},
                       context_instance = RequestContext(request))
def Cordinador_borrar (request, id):
    cordinador_borrar = get_object_or_404(Coordinador, pk=id)
    cordinador_borrar.delete()
    return HttpResponseRedirect("/cordinadoresList/")

def Escuelas(request):
    escuelas = Escuela.objects.all()
    titulo = "Lista de Escuelas"
    return render_to_response('academicos/escuelasList.html',
                              {'escuelas':escuelas,'titulo':titulo},
                          context_instance=RequestContext(request))

def Escuela_add (request):
    if request.method == "POST":
        formulario = EscuelaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/escuelaList/')
    else:
        formulario = EscuelaForm()
    return render_to_response('academicos/escuelasAdd.html',
                        {'formulario':formulario},
                        context_instance=RequestContext(request))
def Escuela_edit (request, id):
        escuela_edit= Escuela.objects.get(pk=id)
        if request.method == 'POST':
           formulario = EscuelaForm(
               request.POST, instance = escuela_edit)
           if formulario.is_valid():
               formulario.save()
               return HttpResponseRedirect("/escuelaList/")
        else:
            formulario = EscuelaForm(instance= escuela_edit)
        return render_to_response('academicos/escuelasEdit.html',
                                 {'formulario': formulario},
                     context_instance = RequestContext(request))
def Escuelas_borrar (request, id):
    escuelas_borrar = get_object_or_404(Escuela, pk=id)
    escuelas_borrar.delete()
    return HttpResponseRedirect("/escuelaList/")

def Facultades(request):
    facultades = Facultad.objects.all()
    titulo = "Lista de Facultades"
    return render_to_response('academicos/facultadList.html',{
                        'facultades':facultades,'titulo':titulo},
                         context_instance=RequestContext(request))

def Facultad_add(request):
    if request.method == "POST":
        formulario = FacultadForm(request.POST)
        if formulario.is_valid():
           formulario.save()
           return HttpResponseRedirect('/facultadesList/')
    else:
        formulario = FacultadForm()
    return render_to_response('academicos/facultadAdd.html',
                             {'formulario': formulario},
                      context_instance = RequestContext(request))

def Facultad_edit (request, id):
        facultad_edit= Facultad.objects.get(pk=id)
        if request.method == 'POST':
            formulario = FacultadForm(
                request.POST, instance = facultad_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/facultadesList/")
        else:
            formulario = FacultadForm(instance= facultad_edit)
        return render_to_response('academicos/facultadEdit.html',
                                 {'formulario': formulario},
                       context_instance = RequestContext(request))
def Facultad_borrar (request, id):
    facultad_borrar = get_object_or_404(Facultad, pk=id)
    facultad_borrar.delete()
    return HttpResponseRedirect("/facultadesList/")

