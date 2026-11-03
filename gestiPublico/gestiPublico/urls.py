"""
URL configuration for gestiPublico project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from django.urls import path

from sitio1.views import  formulario_view, objeto_view, primeravistaweb, recibir_formulario
from sitio1.views import cargamosMensaje
# from sitio1.controllers.people_controller import index as people_index
from sitio1.controllers.people_controller import *
from sitio1.controllers.providers_controller import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', primeravistaweb),
    path('cm/', cargamosMensaje),
    path('objeto/', objeto_view),
    path('formulario/', formulario_view),
    path('enviar/', recibir_formulario, name='recibir_formulario'),
    # path('people/', 
    #      people_index, name='people.index')

    path('people/', index),
    path('people/create/', create),
    path('people/store/', store),
    path('people/<int:id>/', show),
    path('people/<int:id>/edit/', edit),
    path('people/<int:id>/update/', update),
    path('people/<int:id>/destroy/', destroy),
    
    path('providers/', index),
    path('providers/create/', create),
    path('providers/store/', store),
    path('providers/<int:id>/', show),
    path('providers/<int:id>/edit/', edit),
    path('providers/<int:id>/update/', update),
    path('providers/<int:id>/destroy/', destroy),


]
