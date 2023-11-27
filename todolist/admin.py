from django.contrib import admin

from todolist import models


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        "content", "created_at", "deadline", "status",
    )
    list_filter = ("tags",)


admin.site.register(models.Tag)
