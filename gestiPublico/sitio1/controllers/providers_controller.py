from django.shortcuts import render
from sitio1.models.providers import providers

def index(request):
    return render(request, 'providers/index.html')
