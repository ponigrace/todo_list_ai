from django.db import IntegrityError
from django.shortcuts import render, redirect
from .ai_util import AITodo
from .models import Todo
from .forms import CreateTodoForm


# Create your views here.

def home(request):
    todos = Todo.get_todo_list()
    create_todo_form = CreateTodoForm()
    context = {
        'error': '',
        'todos': todos,
        'create_todo_form': create_todo_form,
    }
    return render(request, 'todo.html', context=context)


def create_todo(request):
    if request.method == 'POST':
        create_todo_form = CreateTodoForm(request.POST)
        if create_todo_form.is_valid():
            todo_title = create_todo_form.cleaned_data.get('title')
            response = AITodo().generate_llm_response(todo_title)
            try:
                new_todo = Todo(
                    title=todo_title,
                    llm_response=response
                )
                new_todo.save()
            except IntegrityError:
                error = 'Failed to add a new TODO. Please try again.'
                todos = Todo.get_todo_list()
                create_todo_form = CreateTodoForm()
                context = {
                    'todos': todos,
                    'create_todo_form': create_todo_form,
                    'error': error
                }
                return render(request, 'todo.html', context=context)

    return redirect('home')
