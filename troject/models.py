from django.db import models


class Task(models.model):
    status = models.BooleanField(default=True)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status
