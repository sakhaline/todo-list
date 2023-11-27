from django.contrib import admin
from django.urls import path

from todolist import views

urlpatterns = [
    path("", views.TaskListView.as_view(), name="task-list"),
    path("create/", views.TaskCreateView.as_view(), name="task-create"),
    # path("<int:pk>/update/", views.TaskUpdateView.as_view(), name="task-update"),
    # path("<int:pk>/delete/", views.TaskDeleteView.as_view(), name="task-delete"),

    path("tags/", views.TagListView.as_view(), name="tag-list"),
    # path("tags/create/", views.TagCreateView.as_view(), name="tag-create"),
    # path("tags/<int:pk>/update/", views.TagUpdateView.as_view(), name="tag-update"),
    # path("tags/<int:pk>/delete/", views.TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "todolist"
