from django.shortcuts import redirect, render
from sitio1.models.providers import providers

def index(request):
    return render(request, 'providers/index.html')

def create(request):
    return render(
        request,
        'providers/create.html'
    )

def store(request):
    if request.method == 'POST':
        providers.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone']
        )
        return redirect('/providers')

def show(request, id):
    provider = providers.objects.get(id=id)
    return render(
        request,
        'providers/show.html',
        {
            'provider': provider
        }
    )

def edit(request, id):
    provider = providers.objects.get(id=id)
    return render(
        request,
        'providers/edit.html',
        {
            'provider': provider
        }
    )

def update(request, id):
    provider = providers.objects.get(id=id)
    if request.method == 'POST':
        provider.name = request.POST['name']
        provider.email = request.POST['email']
        provider.phone = request.POST['phone']
        provider.save()
        return redirect('/providers')

def destroy(request, id):
    provider = providers.objects.get(id=id)
    provider.delete()
    return redirect('/providers')

