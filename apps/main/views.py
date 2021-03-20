from django.shortcuts import render
from .models import Person
# Create your views here.

def index(request):
    pl = Person.objects.all() 
    ctx = {'persons_list': pl}
    return render(request, 'index.html', ctx)

def createPerson(request):
    return render(request, 'create_person.html')