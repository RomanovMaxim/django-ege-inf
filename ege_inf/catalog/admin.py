from django.contrib import admin
from .models import Topic, Task, Course, Lesson, LessonTasks

admin.site.register(Topic)
admin.site.register(Task)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(LessonTasks)
