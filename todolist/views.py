from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic

from todolist.models import Task, Tag
from todolist.forms import TaskForm





class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("todolist:task-list")


class TaskListView(generic.ListView):
    model = Task
    fields = "__all__"
    queryset = Task.objects.prefetch_related("tags")


class TaskUpdateView(generic.UpdateView):
    form_class = TaskForm
    queryset = Task.objects.prefetch_related("tags")
    template_name = "todolist/task_form.html"
    success_url = reverse_lazy("todolist:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    fields = "__all__"
    template_name = "todolist/task_confirm_delete.html"
    success_url = reverse_lazy("todolist:task-list")


class TagListView(generic.ListView):
    model = Tag
    fields = "__all__"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todolist:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    fields = "__all__"
    template_name = "todolist/tag_confirm_delete.html"
    success_url = reverse_lazy("todolist:tag-list")


def update_status_view(request, pk):
    task = Task.objects.get(id=pk)
    task.status = not task.status
    task.save()

    return HttpResponseRedirect(reverse("todolist:task-list"))