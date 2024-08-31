from django.urls import path
from . import views

urlpatterns = [
    path("", views.TasksView.as_view(), name="index"),
    # path("criar/", views.criar, name="criar"),
    path('tasks/create/', views.TaskCreate.as_view(), name='create'),
    path("tasks/visualizar/<int:id>", views.visualizar, name="visualizar"),
    path("tasks/editar/<int:id>", views.editar, name="editar"),
    path("tasks/excluir/<int:id>", views.excluir, name="excluir"),
    path("tasks/concluir/<int:id>", views.concluir, name="concluir")
]