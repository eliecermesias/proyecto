from pathlib import Path
from django.shortcuts import render

from django.http import HttpResponse
from django.contrib.auth.views import LoginView

# Create your views here.


# def inicio(request):
#     page = Path(__file__).with_name("index.html").read_text(encoding="utf-8")
#     return HttpResponse(page)

def cargamosMensaje(request):
    return HttpResponse("Este es un mensaje cargado desde la vista cargamosMensaje.")

def primeravistaweb(request):
    return render(request, "index.html")

def formulario_view(request):
    return render(request, "formulario.html")

def recibir_formulario(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        return HttpResponse(f"Datos recibidos: {nombre}, {email}")
    return HttpResponse("Método no permitido")


def objeto_view(request):
    # Crear un objeto de ejemplo
    objeto = {
        'nombre': 'Colecionable de musica',
        'descripcion': 'guitarra de slash.',
        'precio': 12000000.99,
        'disponible': True
    }    
    # Pasar el objeto al contexto de la plantilla
    return render(request, "objeto.html", {'objeto': objeto})

class CustomLoginView(LoginView):
    template_name = 'django_auth_app/login.html'

    def get_success_url(self):
        # Busca 'next' en los datos POST (enviados por el formulario) o en la URL GET
        next_url = self.request.POST.get('next') or self.request.GET.get('next')
        if next_url:
            return next_url
        # Si no hay 'next', usa la redirección por defecto (puedes apuntar a donde quieras)
        return super().get_success_url()