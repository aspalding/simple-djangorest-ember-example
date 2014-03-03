from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=350)
    isCompleted = models.BooleanField(default=False)