from django.db import models
from django.contrib.auth.models import User
from asistentes.models import Persona

GENERO=(
    ('M', 'Masculino'),
    ('F', 'Femenino'),
 )

class Usuario(User):
    persona=models.OneToOneField(Persona)
    sexo=models.CharField(max_length=1, choices=GENERO)
    E_mail=models.CharField(max_length=50)
    def __unicode__(self):
        return '%s  %s ' %(self.persona.nombre, self.persona.apellido_pat)
