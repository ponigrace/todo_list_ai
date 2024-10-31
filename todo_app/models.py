from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=300)
    status = models.BooleanField(default=False)
    llm_response = models.TextField()

    def __str__(self):
        return self.title

    @staticmethod
    def get_todo_list():
        return Todo.objects.all()

