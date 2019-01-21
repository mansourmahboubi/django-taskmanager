from django.conf.urls import url
from .views import task_list, Taskcreate, TaskDelete, change_status

urlpatterns = [
    url(r'^$', task_list, name='tasklist'),
    url(r'^edit/create/$', Taskcreate.as_view(), name='list_update'),
    url(r'^edit/delete/(?P<pk>\d+)', TaskDelete.as_view(), name='list_update'),
    url(r'^edit/status/(?P<pk>\d+)$', change_status, name='change_status'),
]
