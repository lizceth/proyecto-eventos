from django.contrib.auth.models import User
from django.shortcuts import render, render_to_response, get_object_or_404
from asistentes.models import Persona, Participante
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
#from django.core.mail import EmailMessage
#from django.contrib.auth.forms import UserCreationForm, AuthentificationForm
#from django.contrib.auth import login, authentificate, logout
#from django.contrib.auth.decorators import login_required
from asistentes.forms import PersonaForm, ParticipanteForm

def Personas(request):
    personas = Persona.objects.all().order_by('-id')
    return render(request, 'asistentes/persona.html',
                  {'personas':personas})

def persona_add (request):
    if request.method == 'POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/personaList/')
    else:
        formulario = PersonaForm()
    return render_to_response('asistentes/persona_add.html',
                              {'formulario':formulario},
                              context_instance=RequestContext(request))

def Persona_edit (request, id):
        persona_edit= Persona.objects.get(pk=id)
        if request.method == 'POST':
            formulario = PersonaForm(request.POST, instance = persona_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/personaList/")
        else:
            formulario = PersonaForm(instance= persona_edit)
        return render_to_response('asistentes/personaEdit.html',
                    {'formulario': formulario},
                    context_instance = RequestContext(request))
def Persona_borrar (request, id):
    persona_borrar = get_object_or_404(Persona, pk=id)
    persona_borrar.delete()
    return HttpResponseRedirect("/personaList/")


def Participantes(request):
    participantes = Participante.objects.all()
    titulo = "Participantes Registrados"
    return render_to_response('asistentes/participantesList.html',{
                     'participantes':participantes,'titulo':titulo},
                      context_instance=RequestContext(request))

def Participantes_add(request):
    if request.method == "POST":
        formulario = ParticipanteForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/participantesList/')
    else:
        formulario = ParticipanteForm()
    return render_to_response('asistentes/participantesAdd.html',
                                {'formulario': formulario},
                                context_instance = RequestContext(request))

def Participantes_edit (request, id):
        participantes_edit= Participante.objects.get(pk=id)
        if request.method == 'POST':
            formulario = ParticipanteForm(request.POST,
                            instance = participantes_edit)
            if formulario.is_valid():
                formulario.save()
                return HttpResponseRedirect("/participantesList/")
        else:
            formulario = ParticipanteForm(instance= participantes_edit)
        return render_to_response('asistentes/participantesEdit.html',
                                  {'formulario': formulario},
                                   context_instance = RequestContext(request))

def Participantes_borrar (request, id):
    participantes_borrar = get_object_or_404(Participante, pk=id)
    participantes_borrar.delete()
    return HttpResponseRedirect("/participantesList/")


