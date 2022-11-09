from dataclasses import fields
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView , DeleteView
from django.urls import reverse_lazy
from .models import todo
# Create your views here.

class TodoListView(ListView):
    model = todo
    template_name = 'home.html'

class TodoCreateView(CreateView):
    model= todo
    template_name = 'todo_create.html'
    fields = "__all__"
    success_url = reverse_lazy('home')

class TodoDeleteView(DeleteView):
    model = todo
    template_name = 'todo_delete.html'
    success_url = reverse_lazy('home')
 