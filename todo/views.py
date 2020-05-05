from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from .models import TodoModel
from django.urls import reverse_lazy

class TodoList(CreateView, ListView):
    template_name = 'list.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
    
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel