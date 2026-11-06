from django.shortcuts import redirect, render

from sitio1.forms import PropertyForm
from sitio1.models.properties import properties

def index(request):
    properties_list = properties.objects.all()
    return render(request, 'properties/index.html', {'properties': properties_list})

def create(request):
    form = PropertyForm(request.POST if request.method == 'POST' else None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/properties/')

    return render(request, 'properties/create.html', {'form': form})