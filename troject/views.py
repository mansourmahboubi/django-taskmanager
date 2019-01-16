from django.shortcuts import render, get_object_or_404, redirect
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
    # limiting the query set to avoid unprivileged deleting
    queryset = Task.objects.all().filter(status=False)
    model = Task
    success_url = '/'

# the main function
# it displays home page with task groups


def task_list(request, pk=None):
    context = {}
    Tasks = Task.objects.all()
    #  predefined groups = [ home, work ,entertainment]
    context['home'] = Tasks.filter(group__title='home')[:5]
    context['work'] = Tasks.filter(group__title='work').order_by('-updated')[:5]
    context['entertainment'] = Tasks.filter(group__title='entertainment').order_by('-updated')[:5]
    return render(request, 'troject/task.html', context)

# call it through a button and it changes task status


def change_status(request, pk):
    task = get_object_or_404(Task, id=pk)
    task.status = not task.status
    task.save()
    return redirect('/')
