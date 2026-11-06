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
from django.urls import path, include
from django.urls import path, include
from sitio1.views import CustomLoginView


from sitio1.views import  formulario_view, objeto_view, primeravistaweb, recibir_formulario
from sitio1.views import cargamosMensaje
# from sitio1.controllers.people_controller import index as people_index
from sitio1.controllers import people_controller, providers_controller, propeties_controller

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),    
    path('accounts/', include('django_auth_app.urls', namespace='django_auth_app')),

    path('admin/', admin.site.urls),
    path('', primeravistaweb),
    path('cm/', cargamosMensaje),
    path('objeto/', objeto_view),
    path('formulario/', formulario_view),
    path('enviar/', recibir_formulario, name='recibir_formulario'),
    # path('people/', 
    #      people_index, name='people.index')

    path('people/', people_controller.index),
    path('people/create/', people_controller.create),
    path('people/store/', people_controller.store),
    path('people/<int:id>/', people_controller.show),
    path('people/<int:id>/edit/', people_controller.edit),
    path('people/<int:id>/update/', people_controller.update),
    path('people/<int:id>/destroy/', people_controller.destroy),
    
    path('providers/', providers_controller.index),
    path('providers/create/', providers_controller.create),
    path('providers/store/', providers_controller.store),
    path('providers/<int:id>/', providers_controller.show),
    path('providers/<int:id>/edit/', providers_controller.edit),
    path('providers/<int:id>/update/', providers_controller.update),
    path('providers/<int:id>/destroy/', providers_controller.destroy),

    path('properties/', propeties_controller.index),
    path('properties/create/', propeties_controller.create, name='properties_create'),


]
