from django.urls import reverse_lazy
from django.views import generic

from todolist.models import Task, Tag
from todolist.forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"
    queryset = Task.objects.prefetch_related("tags")
    print(queryset)


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"


class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("todolist:task-list")


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")