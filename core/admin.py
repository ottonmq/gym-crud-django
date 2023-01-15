from django.contrib import admin
from .models import usuario,Curso,rutinas,comentario,noticias, documento,Profile

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
  search_fields=('user',)
  list_filter=('user',)

class documentoAdmin(admin.ModelAdmin):
 list_display=('user','info')
 search_fields=('info',)
 list_filter=('info',)
  
class usuarioAdmin(admin.ModelAdmin):
  list_display=('user','nombre','apellidos','sexo','curso','dui','fecha_pago','dui_y_fecha_pago')
  list_display_links=('user','nombre','apellidos','sexo','fecha_pago')
  list_editable=('curso','dui',)
  search_fields=['nombre',]
  list_filter=("fecha_pago","curso")

  def dui_y_fecha_pago(self,obj):
    return "{} - {}".format(obj.dui,obj.fecha_pago)
    

admin.site.register(Curso)
admin.site.register(usuario, usuarioAdmin)
admin.site.register(rutinas)
admin.site.register(comentario)
admin.site.register(noticias)
admin.site.register(documento, documentoAdmin)
admin.site.register(Profile,ProfileAdmin)


#admin.site.unregister(documento)

admin.site.site_header="Administracion gym ottoApp"
admin.site.index_title="gym ottoApp"
admin.site.site_title="otto gym ottoApp"