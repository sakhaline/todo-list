from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __str__(self) -> str:
        return f"#{self.name}"


class Task(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, related_name="tasks")

    class Meta:
        ordering = ("status",)

    def __str__(self) -> str:
        return self.content
