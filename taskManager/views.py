import base64
import io

import matplotlib.pyplot as plt
import openpyxl
from django.shortcuts import render, redirect

from taskManager.dtos import TaskDTO, WorkerDTO
from taskManager.forms import TaskForm, WorkerForm
from taskManager.models import Task, Worker


# Return all tasks data
def task_list(request):
    tasks = list()
    for task in Task.objects():
        tasks.append(TaskDTO(task.id.__str__(), task.name, task.additional_info, task.priority, task.complete).__dict__)
    return render(request, "task-list.html", {'tasks': tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form_data = form.data
            task = Task()
            task.name = form_data.get("name")
            task.additional_info = form_data.get("additional_info")
            task.priority = form_data.get("priority")
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'task-create.html', {'form': form})


def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(initial={'name': task.name, 'additional_info': task.additional_info, 'priority': task.priority})
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form_data = form.data
            task.name = form_data.get("name")
            task.additional_info = form_data.get("additional_info")
            task.priority = form_data.get("priority")
            task.save()
            return redirect('task-list')
    return render(request, 'task-update.html', {'form': form})


def task_delete(request, task_id):
    Task.objects.get(id=task_id).delete()
    return redirect('task-list')


def task_toggle(request, task_id):
    task = Task.objects.get(id=task_id)
    task.complete = not task.complete
    task.save()
    return redirect('task-list')
