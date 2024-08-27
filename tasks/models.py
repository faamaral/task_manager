from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    completed = models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)