from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["title", "description", "due_date"]
        widgets={
            "due_date":forms.SelectDateWidget(attrs={'style': 'display: inline;justify-content: space-between; width: 25%;margin:0px 4px'})
        }