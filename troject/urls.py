from django.conf.urls import url
from .views import TaskListView, task_list, Taskcreate, TaskDelete


urlpatterns = [
    url(r'^test', TaskListView.as_view(), name='task-list'),
    url(r'^create/(?P<pk>\d+)$', Taskcreate.as_view(), name='list_update'),
    url(r'^delete/(?P<pk>\d+)$', TaskDelete.as_view(), name='list_update'),
    url(r'^$', task_list, name='tasklist'),
]
