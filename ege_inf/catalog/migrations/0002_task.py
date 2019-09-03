# Generated by Django 2.2.1 on 2019-09-01 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.TextField()),
                ('answer_text', models.CharField(max_length=50)),
                ('detail_solution_text', models.TextField()),
                ('type_of_task_text', models.CharField(max_length=100)),
                ('year_of_task_text', models.CharField(max_length=100)),
                ('necessary_topics', models.CharField(max_length=100)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('publication_date', models.DateTimeField(verbose_name='date published')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Topic')),
            ],
        ),
    ]
