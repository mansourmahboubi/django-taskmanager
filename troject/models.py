from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings


class Group(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Task(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default="1")
    group = models.ForeignKey(Group)
    status = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.status:
            return "Done"
        return "Pending"

    def get_absolute_url(self):
        return reverse('troject:tasklist')
