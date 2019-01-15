from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Task


# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/
class TaskListView(ListView):
    model = Task


# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/
class Taskcreate(CreateView):
    model = Task
    fields = ['group', 'title']


class TaskDelete(DeleteView):
    model = Task
    success_url = '/'

# the main function
# it displays home page with task groups
# and also is responsible for change status requests


def task_list(request, pk=None):
    if pk:
        task = get_object_or_404(Task, id=pk)
        task.status = not task.status
        task.save()
    context = {}
    Tasks = Task.objects.all()
    #  predefined groups = [ home, work ,entertainment]
    context['home'] = Tasks.filter(group__title='home')[:5]
    context['work'] = Tasks.filter(group__title='work')[:5]
    context['entertainment'] = Tasks.filter(group__title='entertainment')[:5]
    return render(request, 'troject/task.html', context)
