from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(verbose_name="Título",max_length=250)
    description = models.TextField(verbose_name="Descrição")
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(verbose_name="Data para finalização")
    user = models.ForeignKey(User, on_delete=models.CASCADE)