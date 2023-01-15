from django.db import models
from django.contrib.auth.models import User
from	django.conf	import	settings
# Create your models here.

class Curso(models.Model):
  entrenamiento = models.CharField(max_length=100,unique=True)
  precio = models.CharField(max_length=10)
  horario = models.CharField(max_length=200)
  def __str__(self):
    return self.entrenamiento
    
class usuario(models.Model):
  nombre = models.CharField(max_length=100)
  apellidos = models.CharField(max_length=100)
  SEXOS = (('F','Femenino'),('M','Masculino'))
  sexo = models.CharField(max_length=1,choices=SEXOS,default='Masculino')
  dui = models.IntegerField()
  curso = models.ForeignKey(Curso,null=False,blank=False,on_delete=models.CASCADE)
  fecha_pago = models.DateTimeField()
  user = models.ForeignKey(User,on_delete= models.CASCADE)
  def __str__(self):
    return self.nombre

    
  
  
class rutinas(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  nombre = models.CharField(max_length=100)
  info = models.CharField(max_length=500)
  def __str__(self):
   return self.nombre
  class Meta: 
   verbose_name = "rutina"
   verbose_name_plural = "rutinas"

class comentario(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE)
  TIPOS = (('Reclamo','Reclamo'),('Sugerencia','Sugerencia'),('Solicitud','Solicitud'))
  tipo = models.CharField(max_length=100,choices=TIPOS,default='Sugerencia')
  info = models.CharField(max_length=500)
  def __str__(self):
    return self.tipo
  
     
class noticias(models.Model):
  info = models.CharField(max_length=500)
  
  def __str__(self):
    return self.info
     
  class Meta:
    verbose_name = 'noticias'
    verbose_name_plural = "noticias"
     

class documento(models.Model):
     user = models.ForeignKey(User,on_delete= models.CASCADE)
     info = models.CharField(max_length=255, blank=True)
     imagen = models.FileField(upload_to='documents/')
     uploaded_at = models.DateTimeField(auto_now_add=True)
     def __str__(self):
      return self.info
    

class	Profile(models.Model):
			user	=	models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
			cumpleaños =	models.DateField(blank=True,	null=True)
			foto	=	models.FileField(upload_to='users/',blank=True)
			def	__str__(self):
				return	'	datos para	user	{}'.format(self.user.username)