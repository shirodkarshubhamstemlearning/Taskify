from django.db import models
from django.core.exceptions import ValidationError
from django.conf import settings
import datetime

status_choices = [
    ('To Do', 'To Do'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed')
]

class Task(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    desc = models.TextField(null=True, blank=True)
    assignee = models.CharField(max_length=255, null=False, blank=False)
    status = models.CharField(choices=status_choices, default='To Do')
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
