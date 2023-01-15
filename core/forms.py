
from django.contrib.auth.models import User
from django.contrib.auth.forms   import UserCreationForm
from django  import forms

from .models import Curso,usuario,rutinas,comentario, noticias, documento,Profile


class RegistroForm(UserCreationForm):
  class Meta:
    model = User
    fields = [
      'username',
      'first_name',
      'last_name',
      'email',
      ]
    labels = {
      'username' :'nombre de usuario',
      'first_name' : 'nombre',
      'last_name' : 'apellidos',
      'email' : 'correo',
     
    }
    
class PersonaForm(forms.ModelForm):
  class Meta:
    model = Curso
    fields ="__all__"
    
class matriForm(forms.ModelForm):
  class Meta:
    model = usuario
    fields = '__all__'


  
class rutinasForm(forms.ModelForm):
  class Meta:
    model = rutinas
    fields = [
      'nombre',
      'info'
      ]
    labels ={
       'nombre' : 'Nombre de tu rutina',
       'info' : 'descripcion'
      }
    
class comenForm(forms.ModelForm):
  class Meta:
    model = comentario
    fields = [
      'tipo',
      'info'
      ]
    labels ={
       'tipo' : 'tipo de comentario',
       'info' : 'descripcion'
      }
    
class notiForm(forms.ModelForm):
  class Meta:
    model = noticias
    fields = '__all__'
  
class docForm(forms.ModelForm):
  class Meta:
    model = documento
    fields = [
      'info',
      'imagen'
      ]
      

 
