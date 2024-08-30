from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarForm
from .models import Task
from datetime import datetime

class TasksView(LoginRequiredMixin, ListView):
    model=Task
    paginate_by=10

    def get_queryset(self, *args, **kwargs): 
        completed = self.request.GET.get('completed')
        qs = super(TasksView, self).get_queryset(*args, **kwargs) 
        qs = qs.filter(user_id=self.request.user.id).order_by("-id") 
        if completed:
            qs = qs.filter(completed=completed)
        return qs

def index(request):

    return render(request, 'index.html')

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    fields=['title', 'description', 'due_date']
    template_name='tasks/form.html'
    success_url=reverse_lazy('index')

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
                form.save()
                messages.success(request, "Tarefa alterada com sucesso!")
                return redirect(visualizar,id=task.id)
            except Exception as error:
                messages.error(request, f"Erro ao alterar tarefa!\n{str(error)}")
    form = CriarForm(instance=task)
    return render(request, 'criar.html', {"tasks": task, "form": form, "messages": messages})

@login_required
def concluir(request, id):
    try:
        task = Task.objects.get(id=id)
        if task is not None:
            task.completed = True
            task.save()
            messages.success(request, "Tarefa concluida com sucesso!")
    except Exception as error:
        messages.error(request, f"Tarefa não pode ser concluida.\n{str(error)}")
    return redirect("index")


@login_required
def excluir(request, id):
    if request.method == "POST":
        try:
            task = Task.objects.get(id=id)
            task.delete()
            messages.success(request, "Tarefa excluida com sucesso!")
        except Exception as error:
            messages.error(request, "Erro ao excluir a tarefa!\n"+str(error))

    return redirect("index")
