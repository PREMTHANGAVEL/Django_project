from django.shortcuts import render, get_object_or_404, redirect
from .forms import TaskForm
from .services import TaskManager
from .models import Task

task_manager = TaskManager()

def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task_manager.add_task(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                priority=form.cleaned_data['priority'],
                status=form.cleaned_data['status'],
                
                
            )
            return redirect('view_all_tasks')
    else:
        form = TaskForm()
    return render(request, 'tasks/task_form.html', {'form': form})



def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            task_manager.edit_task(
                task_id=task.id,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                priority=form.cleaned_data['priority'],
                status=form.cleaned_data['status']
            )
            return redirect('view_all_tasks')
    else:
        form = TaskForm(instance=task)
    return render(request, 'tasks/task_form.html', {'form': form})

def delete_task(request, task_id):
    if request.method == "POST":
        task_manager.delete_task(task_id)
        return redirect('view_all_tasks')
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'tasks/confirm_delete.html', {'task': task})

def view_all_tasks(request):
    tasks = task_manager.view_all_tasks()
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def filter_tasks_by_priority(request, priority):
    tasks = task_manager.filter_tasks_by_priority(priority)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


