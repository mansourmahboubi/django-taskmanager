from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Task


# https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-display/
class TaskListView(ListView):

    model = Task
