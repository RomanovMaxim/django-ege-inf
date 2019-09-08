# Generated by Django 2.2.1 on 2019-09-08 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='source_of_task_text',
            field=models.CharField(default=1, max_length=100, verbose_name='Источник'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='answer_text',
            field=models.CharField(max_length=50, verbose_name='Ответ'),
        ),
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='task',
            name='detail_solution_text',
            field=models.TextField(verbose_name='Решение'),
        ),
        migrations.AlterField(
            model_name='task',
            name='necessary_topics',
            field=models.CharField(max_length=100, verbose_name='Необходимо знание тем'),
        ),
        migrations.AlterField(
            model_name='task',
            name='publication_date',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_text',
            field=models.TextField(verbose_name='Условие задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Topic', verbose_name='Тема задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='type_of_task_text',
            field=models.CharField(max_length=100, verbose_name='Тип задачи'),
        ),
        migrations.AlterField(
            model_name='task',
            name='year_of_task_text',
            field=models.CharField(max_length=100, verbose_name='Актуальный год'),
        ),
    ]
