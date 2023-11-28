from django.shortcuts import render, redirect, get_object_or_404

from taskManager.dtos import TaskDTO, EmployeeDTO
from taskManager.forms import TaskForm, EmployeeForm, TaskAssignmentForm
from taskManager.models import Task, Employee


# Return all tasks data
def task_list(request):
    filter_by = request.GET.get('filter_by', 'priority')  # Default filter by priority
    order_by = request.GET.get('order', 'asc')  # Default order is ascending

    # Determine the sorting order based on the 'order' query parameter
    if order_by == 'asc':
        order = ''
    elif order_by == 'desc':
        order = '-'

    if filter_by == 'priority':
        tasks = Task.objects.order_by(f'{order}priority')
    elif filter_by == 'type':
        tasks = Task.objects.order_by(f'{order}role')
    elif filter_by == 'complete':
        tasks = Task.objects.order_by(f'{order}complete')
    else:
        tasks = Task.objects()

    # Convert MongoDB documents to TaskDTO instances
    task_dtos = [
        TaskDTO(task.id.__str__(), task.name, task.additional_info, task.priority, task.role, task.complete,
                task.employee).__dict__
        for task in tasks]

    return render(request, "task-list.html", {'tasks': task_dtos, 'filter_by': filter_by})


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
    form = TaskForm(initial={'name': task.name, 'additional_info': task.additional_info, 'priority': task.priority,
                             'role': task.role})
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


def task_view(request, task_id):
    task = Task.objects.get(id=task_id)
    employees = Employee.objects.all()

    if request.method == 'POST':
        employee_id = request.POST.get('employee')
        if employee_id:
            employee = Employee.objects.get(id=employee_id)
            task.employee = employee
        else:
            task.employee = None
        task.save()
        return redirect('task-list')

    task_dto = TaskDTO(
        task_id=str(task.id),
        name=task.name,
        additional_info=task.additional_info,
        priority=task.priority,
        role=task.role,
        complete=task.complete,
        employee=EmployeeDTO(
            employee_id=str(task.employee.id) if task.employee else None,
            name=task.employee.name if task.employee else None,
            surname=task.employee.surname if task.employee else None,
            role=task.employee.role if task.employee else None
        )
    )

    employee_dtos = []
    for employee in employees:
        employee_dto = EmployeeDTO(
            employee_id=str(employee.id),
            name=employee.name,
            surname=employee.surname,
            role=employee.role
        )
        employee_dtos.append(employee_dto)

    return render(request, 'task-view.html', {'task_dto': task_dto, 'employee_dtos': employee_dtos})


def connect_employee(request, task_id, employee_id):
    task = Task.objects.get(id=task_id)
    employee = Employee.objects.get(id=employee_id)

    # Connect the selected employee to the task
    task.employee = employee
    task.save()

    return redirect('task-view', task_id=task_id)  # Redirect back to the task detail page


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
