from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task, Group
from .forms import LoginForm


class Taskcreate(LoginRequiredMixin, CreateView):
    # https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/
    model = Task
    fields = ['group', 'title']

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        request.POST['user'] = self.request.user.id
        return super(Taskcreate, self).post(request, **kwargs)


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = '/'

    # limiting the query set to avoid unprivileged deleting
    def get_queryset(self):
        queryset = super(TaskDelete, self).get_queryset()
        return queryset.filter(status=False, user__id=self.request.user.id)


@login_required
def task_list(request):
    # the main function
    # it displays home page with task groups
    context = {}
    tasks = Task.objects.filter(user__id=request.user.id).order_by('-updated')
    groups = Group.objects.values_list('title', flat=True)
    context['groups'] = groups
    context['first'] = tasks.filter(group__title=groups[0])
    context['second'] = tasks.filter(group__title=groups[1])
    context['third'] = tasks.filter(group__title=groups[2])
    return render(request, 'troject/task.html', context)


def signin(request):
    loginform = LoginForm(request.POST or None)
    if loginform.is_valid():
        username = loginform.cleaned_data.get("username")
        password = loginform.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'login.html', {"loginform": loginform})


def change_status(request, pk):
    # call it through a button and it changes task status
    task = get_object_or_404(Task, id=pk, user__id=request.user.id)
    task.status = not task.status
    task.save()
    return redirect('/')
