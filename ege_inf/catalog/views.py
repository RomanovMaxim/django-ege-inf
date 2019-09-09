from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Topic, Task, Course, Lesson, LessonTasks

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

def lesson_detail(request, pk):
    lesson_task_list = LessonTasks.objects.filter(lesson=pk)
    latest_task_list = []
    for lesson_task in lesson_task_list:
        task = get_object_or_404(Task, pk=lesson_task.task.pk)
        latest_task_list.append(task)
    return render(request, 'catalog/lesson.html', context={'latest_task_list':latest_task_list,})



class CourseView(generic.ListView):
    template_name = 'catalog/course.html'
    context_object_name = 'lesson_list'

    def get_queryset(self):
       return Lesson.objects.all()

# def course(request):
#     return render(request, 'catalog/course.html',{})
