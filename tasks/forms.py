from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from .models import Task
from task_manager import settings

class CriarForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["title", "description", "due_date"]
        widgets={
            "due_date":forms.SelectDateWidget(attrs={'style': 'display: inline;justify-content: space-between; width: 25%;margin:0px 4px'})
        }
    # title = forms.CharField(label="Título", max_length=250, required=True)
    # description = forms.CharField(label="Descrição", widget=forms.Textarea(attrs={"rows":"5"}), required=True)
    # due_date = forms.DateField(label="Data para conclusão",widget=forms.SelectDateWidget(),required=True)