from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.list import ListView
from .forms import CriarForm
from .models import Task
from datetime import datetime

class TasksView(ListView):
    model=Task

    def get_queryset(self, *args, **kwargs): 
        qs = super(TasksView, self).get_queryset(*args, **kwargs) 
        qs = qs.order_by("-id") 
        return qs

def index(request):

    return render(request, 'index.html', )

@login_required
def criar(request):
    if request.method == "POST":
        form = CriarForm(request.POST)
        if form.is_valid():
            try:
                task = Task(
                    title=form.cleaned_data["title"], 
                    description=form.cleaned_data["description"],
                    due_date=form.cleaned_data["due_date"],
                    created_at=datetime.now,
                    user_id=1)
                task.save()
                messages.success(request, "Tarefa criada com sucesso!")
                return redirect(visualizar,id=task.id)
            except Exception as error: 
                messages.error(request, f"Erro ao criar a tarefa!\n"+str(error))
    return render(request, "criar.html", {'criar_form': CriarForm()})

@login_required
def visualizar(request, id):
    usuario = request.user
    task = Task.objects.get(id=id)
        
    return render(request, "visualizar.html", {"tasks": task})

@login_required
def editar(request, id):
    task = Task.objects.get(id=id)
    if request.method == "POST":
        form = CriarForm(request.POST, instance=task)
        if form.is_valid():
            try:
                task.title = form.cleaned_data["title"]
                task.description = form.cleaned_data["description"]
                task.due_date = form.cleaned_data["due_date"]
                task.save()
                messages.success(request, "Tarefa alterada com sucesso!")
                return redirect(visualizar,id=task.id)
            except Exception as error:
                messages.error(request, f"Erro ao alterar tarefa!\n"+str(error))
    return render(request, 'criar.html', {"tasks": task})

@login_required
def excluir(request, id):
    if request.method == "POST":
        try:
            task = Task.objects.get(id=id)
            task.delete()
            messages.success(request, "Tarefa excluida com sucesso!")
        except Exception as error:
            messages.error(request, f"Erro ao excluir a tarefa!\n"+str(error))

    return redirect(index)
