from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='task', blank=True, null=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    about = models.TextField(max_length=200, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    description = models.TextField(max_length=400, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    processing = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.description

