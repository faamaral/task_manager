from django.urls import path
from . import views

urlpatterns = [
    path("", views.TasksView.as_view(), name="index"),
    path("criar/", views.criar, name="criar"),
    path('create/', views.TaskCreate.as_view(), name='create'),
    path("visualizar/<int:id>", views.visualizar, name="visualizar"),
    path("editar/<int:id>", views.editar, name="editar"),
    path("excluir/<int:id>", views.excluir, name="excluir"),
    path("concluir/<int:id>", views.concluir, name="concluir")
]