from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Task, Group


# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/
class TaskListView(ListView):
    model = Task


# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/
class Taskcreate(CreateView):
    model = Task
    fields = ['group', 'title']


class TaskDelete(DeleteView):
    model = Task


def task_list(request):
    context = {}
    Tasks = Task.objects.all()
    #  predefined groups = [ todo, doing ,done]
    context['todo'] = Tasks.filter(group__title='todo')[:5]
    context['doing'] = Tasks.filter(group__title='doing')[:5]
    context['done'] = Tasks.filter(group__title='doing')[:5]
    return render(request, 'troject/task.html', context)
