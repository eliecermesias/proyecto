from django.shortcuts import redirect, render
from sitio1.models.people import people
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    persons = people.objects.all()
    return render(request, 'people/index.html', {'persons': persons})

def create(request):

    return render(
        request,
        'people/create.html'
    )


def store(request):

    if request.method == 'POST':

        people.objects.create(
            name=request.POST['name'],
            age=request.POST['age'],
            email=request.POST['email']
        )

        return redirect('/people')


def show(request, id):

    person = people.objects.get(id=id)

    return render(
        request,
        'people/show.html',
        {
            'person': person
        }
    )


def edit(request, id):

    person = people.objects.get(id=id)

    return render(
        request,
        'people/edit.html',
        {
            'person': person
        }
    )


def update(request, id):

    person = people.objects.get(id=id)

    if request.method == 'POST':

        person.name = request.POST['name']
        person.age = request.POST['age']
        person.email = request.POST['email']

        person.save()

    return redirect('/people')


def destroy(request, id):

    person = people.objects.get(id=id)

    person.delete()

    return redirect('/people')