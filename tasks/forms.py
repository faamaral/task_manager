from django import forms
from .models import Task
from task_manager import settings

class CriarForm(forms.Form):
    # class Meta:
    #     model=Task
    #     fields=["title", "description", "due_date"]
    title = forms.CharField(label="Título", max_length=250, required=True)
    description = forms.CharField(label="Descrição", widget=forms.Textarea(attrs={"rows":"5"}), required=True)
    due_date = forms.DateField(label="Data para conclusão",widget=forms.SelectDateWidget(),required=True)