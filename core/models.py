from random import choices
from django.db import models

from django.utils import timezone
from django.urls import reverse


MAX_LENGTH = 100
TODO_STATUS_ASSIGNED = 'assigned'
TODO_STATUS_IN_PROGRESS = 'in-progress'
TODO_STATUS_COMPLETED = 'completed'
TODO_STATUS_CHOICES = [
    (TODO_STATUS_ASSIGNED, TODO_STATUS_ASSIGNED.title()),
    (TODO_STATUS_IN_PROGRESS, TODO_STATUS_IN_PROGRESS.title()),
    (TODO_STATUS_COMPLETED, TODO_STATUS_COMPLETED.title())
]


class ToDoItem(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    description = models.TextField()
    status = models.CharField(max_length=MAX_LENGTH, choices=TODO_STATUS_CHOICES)
    completion_date = models.DateTimeField(null=True, blank=True)    

    def __str__(self):
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]
