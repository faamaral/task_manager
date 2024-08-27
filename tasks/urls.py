from django.urls import path

from . import views

urlpatterns = [
    path("", views.TasksView.as_view()),
    path("criar/", views.criar, name="criar"),
    path("visualizar/<int:id>", views.visualizar, name="visualizar"),
    path("editar/", views.editar, name="editar"),
    path("excluir/", views.excluir, name="excluir")
]