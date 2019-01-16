from django.contrib import admin
from .models import Task, Group


class GroupAdmin(admin.ModelAdmin):
    list_display = ['title', 'updated']


class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'group', 'updated', 'status']


admin.site.register(Task, TaskAdmin)
admin.site.register(Group, GroupAdmin)
