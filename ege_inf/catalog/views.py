from django.shortcuts import render
from django.views import generic

from .models import Topic, Task


class IndexView(generic.ListView):
    #template_name = 'catalog/index.html'
    #context_object_name = ''
    model = Task
