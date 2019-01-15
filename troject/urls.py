from django.conf.urls import url
from .views import TaskListView, task_list, Taskcreate, TaskDelete

urlpatterns = [
    url(r'^test', TaskListView.as_view(), name='task-list'),
    url(r'^edit/create/$', Taskcreate.as_view(), name='list_update'),
    url(r'^edit/delete/(?P<pk>\d+)', TaskDelete.as_view(), name='list_update'),
    url(r'^$', task_list, name='tasklist'),
    url(r'^(?P<pk>\d+)$', task_list, name='change_status'),
]
