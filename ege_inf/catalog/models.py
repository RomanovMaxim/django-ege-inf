from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    topic_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.topic_text


class Task(models.Model):
    topic = models.ForeignKey(
        Topic,
        on_delete=models.CASCADE,
        verbose_name="Тема задачи"
    )
    task_text = models.TextField('Условие задачи')
    answer_text = models.CharField('Ответ', max_length=50)
    detail_solution_text = models.TextField('Решение')
    type_of_task_text = models.CharField('Тип задачи',max_length=100)
    author_of_task = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    source_of_task_text = models.CharField('Источник',max_length=100)
    year_of_task_text = models.CharField('Актуальный год',max_length=100)

    # "Необходимые темы" нужно брать из имеющихся "Тем"
    necessary_topics = models.CharField('Необходимо знание тем',max_length=100)

    creation_date = models.DateTimeField('Дата создания')
    publication_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.task_text


class Course(models.Model):
    course_text = models.CharField('Название', max_length=200)
    author_of_course = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    creation_date = models.DateTimeField('Дата создания')
    publication_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.course_text

class Lesson(models.Model):
    lesson_text = models.CharField('Название', max_length=200)
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Курс"
    )
    author_of_lesson = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор"
    )
    creation_date = models.DateTimeField('Дата создания')
    publication_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.lesson_text

class LessonTasks(models.Model):
    lesson =  models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Урок"
    )
    task =  models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        verbose_name="Задача"
    )
    def __str__(self):
        return "{} : {}".format(self.lesson, self.task)
