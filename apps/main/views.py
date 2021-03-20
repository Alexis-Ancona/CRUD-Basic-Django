from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from .models import Person
from .forms import PersonForm
# Create your views here.

#/
class PersonList(ListView):
    model = Person
    template_name = 'index.html'
#/create/
class PersonCreate(CreateView):
    model = Person
    form_class = PersonForm
    template_name = 'create_person.html'
    success_url = reverse_lazy('index')
#/update
class PersonUpdate(UpdateView):
    model = Person
    form_class = PersonForm
    template_name = 'create_person.html'
    success_url = reverse_lazy('index')

class PersonDelete(DeleteView):
    model = Person
    template_name = 'person_confirm_delete.html'
    success_url = reverse_lazy('index')