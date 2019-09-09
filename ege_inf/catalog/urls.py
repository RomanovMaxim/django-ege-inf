from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    # ex: /catalog/
    path('', views.index, name='index'),
    #path('', views.IndexView.as_view(), name='index'),
    path('lesson/', views.LessonView.as_view(), name='lesson'),
    #path('lesson/', views.lesson, name='lesson'),
    #path('course/', views.course, name='course'),
    path('course/', views.CourseView.as_view(), name='course'),
    path('lesson/<int:pk>/', views.lesson_detail, name='lesson_detail'),
]
