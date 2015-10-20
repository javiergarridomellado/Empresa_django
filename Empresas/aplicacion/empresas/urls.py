from django.conf.urls import patterns, include, url
from .views import RegistrarEmpresa, RedirigirEmpresa



urlpatterns = patterns('',
  
    url(r'^registrar/$' , RegistrarEmpresa.as_view() , name="registrar_empresa" ),
    url(r'^redirigir/$' , RedirigirEmpresa.as_view() , name="redirigir_empresa" ),
    

)