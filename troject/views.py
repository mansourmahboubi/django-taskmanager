from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Task, Group


class Taskcreate(CreateView):
    # https://docs.djangoproject.com/en/1.11/ref/class-based-views/generic-editing/
    model = Task
    fields = ['group', 'title']

    def post(self, request, **kwargs):
        request.POST = request.POST.copy()
        request.POST['user'] = self.request.user.id
        return super(Taskcreate, self).post(request, **kwargs)


class TaskDelete(DeleteView):
    model = Task
    success_url = '/'

    # limiting the query set to avoid unprivileged deleting
    def get_queryset(self):
        queryset = super(TaskDelete, self).get_queryset()
        return queryset.filter(status=False, user__id=self.request.user.id)


def task_list(request):
    # the main function
    # it displays home page with task groups
    if not request.user.is_authenticated:
        return render(request, 'login.html', {})
    context = {}
    tasks = Task.objects.filter(user__id=request.user.id).order_by('-updated')
    groups = Group.objects.values_list('title', flat=True)
    context['groups'] = groups
    context['first'] = tasks.filter(group__title=groups[0])
    context['second'] = tasks.filter(group__title=groups[1])
    context['third'] = tasks.filter(group__title=groups[2])
    return render(request, 'troject/task.html', context)


def change_status(request, pk):
    # call it through a button and it changes task status
    task = get_object_or_404(Task, id=pk, user__id=request.user.id)
    task.status = not task.status
    task.save()
    return redirect('/')
