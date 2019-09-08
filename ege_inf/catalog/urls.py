from django.urls import path

from . import views

app_name = 'catalog'
urlpatterns = [
    # ex: /catalog/
    path('', views.index, name='index'),
    #path('', views.IndexView.as_view(), name='index'),
    path('lesson/', views.LessonView.as_view(), name='lesson'),
    #path('lesson/', views.lesson, name='lesson'),
]
