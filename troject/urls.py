from django.conf.urls import url
from .views import TaskListView


urlpatterns = [
    url(r'^$', TaskListView.as_view(), name='task-list'),
]
