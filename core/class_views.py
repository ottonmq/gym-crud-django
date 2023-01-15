from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms   import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView,DeleteView,UpdateView

from .forms import PersonaForm,RegistroForm,rutinasForm,comenForm,notiForm,docForm

from .models import Curso, usuario,rutinas,comentario,noticias,documento,Profile


  
class RegistroUsuario(CreateView):
  model = User
  form_class = RegistroForm
  template_name = 'core/registrar.html'
  success_url = reverse_lazy('login')
  
  
class registrorutinas(CreateView):
   model : rutinas
   form_class = rutinasForm
   template_name = 'core/usuarios/regrutinas.html'
   success_url = reverse_lazy('usuarios')
   def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(registrorutinas, self).form_valid(form)

  


  
class PersonaList(ListView):
  model = Curso
  template_name ='core/lis.html'
  
class matrilist(ListView):
  model = usuario
  template_name ='core/usuarios/lis2.html'
 
  def get_queryset(self):
    return self.model.objects.filter(user=self.request.user)
  
class rutinalist(ListView):
   model = rutinas
   template_name = 'core/usuarios/rutinas.html'
   
   def get_queryset(self):
    return self.model.objects.filter(user=self.request.user)
    
  
   
  
class rutinad(DeleteView):
   model = rutinas
   template_name = 'core/usuarios/verifi.html'
   success_url=reverse_lazy('usuarios')
    
  #def get_queryset(self):
    #return self.model.objects.filter(alumnoid__nombre=
    #"Otto Napoleón")

class comentario(ListView):
  model = comentario
  template_name ='core/come.html'
  paginate_by = 2
  context_object_name = 'c'
  
  
class registrocomen(CreateView):
   model : comentario
   form_class = comenForm
   template_name = 'core/usuarios/recomen.html'
   success_url = reverse_lazy('usuarios')
   def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(registrocomen, self).form_valid(form)


class noti(ListView):
  model = noticias
  template_name = 'core/noticias.html'
  paginate_by = 4
  context_object_name = 'c'
  
class documento(ListView):
  model = documento
  template_name ='core/doc.html'
  paginate_by = 1
  context_object_name = 'c'
  
    
  
class doc(ListView):
  model = documento
  template_name ='core/doc1.html'
  paginate_by = 1
  context_object_name = 'c'

class creadoc(CreateView):
  model : documento
  form_class = docForm
  template_name = 'core/redoc.html'
  success_url = reverse_lazy('usuarios')
  def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(creadoc, self).form_valid(form)
 


  
 
 
 



  
 

   

   
               
       
   
   
   
  
  
  
  
  
