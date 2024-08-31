from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import TaskForm
from .models import Task

class TasksView(LoginRequiredMixin, ListView):
    model=Task
    paginate_by=10

    def get_queryset(self, *args, **kwargs): 
        completed = self.request.GET.get('completed')
        qs = super(TasksView, self).get_queryset(*args, **kwargs) 
        qs = qs.filter(user_id=self.request.user.id).order_by("due_date") 
        if completed:
            qs = qs.filter(completed=completed)
        return qs

class TaskCreate(LoginRequiredMixin,CreateView):
    model=Task
    template_name='tasks/form.html'
    success_url=reverse_lazy('index')
    form_class=TaskForm


@login_required
def visualizar(request, id):
    usuario = request.user
    task = get_object_or_404(Task,id=id, user_id=usuario.id)
        
    return render(request, "visualizar.html", {"tasks": task})

@login_required
def editar(request, id):
    try:
        usuario = request.user
        task = get_object_or_404(Task,id=id, user_id=usuario.id)
        if request.method == "POST":
            form = TaskForm(request.POST, instance=task)
            if form.is_valid():
                try:
                    form.save()
                    messages.success(request, "Tarefa alterada com sucesso!")
                    return redirect(visualizar,id=task.id)
                except Exception as error:
                    messages.error(request, f"Erro ao alterar tarefa!\n{str(error)}")
        form = TaskForm(instance=task)
        return render(request, 'criar.html', {"tasks": task, "form": form, "messages": messages})
    except Exception as error:
        messages.error(request, f"Tarefa não encontrada ou Você não possui permissão para edita-la\nErro: {str(error)}")
        return redirect("index")
    

@login_required
def concluir(request, id):
    try:
        usuario = request.user
        task = get_object_or_404(Task,id=id, user_id=usuario.id)
        if task is not None:
            task.complete_task()
            messages.success(request, "Tarefa concluida com sucesso!")
    except Exception as error:
        messages.error(request, f"Tarefa não pode ser concluida.\n{str(error)}")
    return redirect("index")


@login_required
def excluir(request, id):
    if request.method == "POST":
        try:
            usuario = request.user
            task = get_object_or_404(Task,id=id, user_id=usuario.id)
            task.delete()
            messages.success(request, "Tarefa excluida com sucesso!")
        except Exception as error:
            messages.error(request, "Erro ao excluir a tarefa!\n"+str(error))

    return redirect("index")
