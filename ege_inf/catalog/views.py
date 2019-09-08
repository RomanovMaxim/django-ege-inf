from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic

from .models import Topic, Task

# def index(request):
#     latest_task_list = Task.objects.all()
#     output = ', '.join([t.task_text for t in latest_task_list])
#     return HttpResponse(output)

def index(request):
    return render(request, 'catalog/index.html',{})

# class IndexView(generic.ListView):
#     template_name = 'catalog/index.html'
#     #context_object_name = 'latest_task_list'
#
#     #def get_queryset(self):
#     #    return Task.objects.all()


class LessonView(generic.ListView):
    template_name = 'catalog/lesson.html'
    context_object_name = 'latest_task_list'

    def get_queryset(self):
       return Task.objects.all()

# def lesson(request):
#     return render(request, 'catalog/lesson.html',{})
