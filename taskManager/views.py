from django.shortcuts import render, redirect

from taskManager.dtos import TaskDTO, EmployeeDTO
from taskManager.forms import TaskForm, EmployeeForm
from taskManager.models import Task, Employee


# Return all tasks data
def task_list(request):
    tasks = list()
    for task in Task.objects():
        tasks.append(TaskDTO(task.id.__str__(), task.name, task.additional_info, task.priority, task.role, task.complete).__dict__)
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
            task.role = form_data.get("role")
            task.save()
            return redirect('task-list')
    else:
        form = TaskForm()
    return render(request, 'task-create.html', {'form': form})


def task_update(request, task_id):
    task = Task.objects.get(id=task_id)
    form = TaskForm(initial={'name': task.name, 'additional_info': task.additional_info, 'priority': task.priority, 'role': task.role})
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form_data = form.data
            task.name = form_data.get("name")
            task.additional_info = form_data.get("additional_info")
            task.priority = form_data.get("priority")
            task.role = form_data.get("role")
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


def employee_list(request):
    employees = list()
    for employee in Employee.objects():
        employees.append(EmployeeDTO(employee.id.__str__(), employee.name, employee.surname, employee.role).__dict__)
    return render(request, "employee-list.html", {'employees': employees})


def employee_create(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form_data = form.data
            employee = Employee()
            employee.name = form_data.get("name")
            employee.surname = form_data.get("surname")
            employee.role = form_data.get("role")
            employee.save()
            return redirect('employee-list')
    else:
        form = EmployeeForm()
    return render(request, 'employee-create.html', {'form': form})


def employee_update(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    form = EmployeeForm(initial={'name': employee.name, 'surname': employee.surname, 'role': employee.role})
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form_data = form.data
            employee.name = form_data.get("name")
            employee.surname = form_data.get("surname")
            employee.role = form_data.get("role")
            employee.save()
            return redirect('employee-list')
    return render(request, 'employee-update.html', {'form': form})


def employee_delete(request, employee_id):
    Employee.objects.get(id=employee_id).delete()
    return redirect('employee-list')
