"""gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static


from core.class_views import PersonaList,RegistroUsuario,matrilist,rutinalist,registrorutinas,rutinad,comentario,registrocomen,noti,documento,creadoc
urlpatterns = [
    path('',include('core.urls')),
    path('admin/', admin.site.urls),
    path('lis/',PersonaList.as_view(),name='lis'),
    path('registrar/',RegistroUsuario.as_view(),name='registrar'),
    
    path('lis2/',matrilist.as_view(),name='lis2'),
    
    path('rutina/',rutinalist.as_view(),name='rutina'),
    
    path('comentario/',comentario.as_view(),name='comentario'),
    
    path('noti/',noti.as_view(),name='noti'),
    
    

    path('regrutinas/',registrorutinas.as_view(),name='regrutinas'),
    
  
    path('registrocomen/', registrocomen.as_view(),name='registrocomen'),
 
    
    
    path('rutinad/<int:pk>',rutinad.as_view(),name='rutinad'),
    
    path('doc/', documento.as_view(),name='doc'),
    
    
    
    path('regdoc/',creadoc.as_view(),name='regdoc'),
  
   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

