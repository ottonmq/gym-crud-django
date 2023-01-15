from django.urls import path
from .views import home,galeria,loc,login,logout, usuarios




urlpatterns = [
    path('', home,name='home'),
    path('galeria/',galeria,name='galeria'),
    path('loc/',loc,name='loc'),
    path('login/',login,name='login'),
    path('logout/',logout,name='logout'),
    path('usuarios/', usuarios,name='usuarios'),
    
    
   # path('rutinas/',rutinas,name='rutinas')
]
