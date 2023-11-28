from django.urls import path

from . import views

urlpatterns = [
    path('task-list', views.task_list, name='task-list'),
    path('task-create', views.task_create, name='task-create'),
    path('task-update/<str:task_id>', views.task_update, name='task-update'),
    path('task-delete/<str:task_id>', views.task_delete, name='task-delete'),
    path('task-toggle-complete/<str:task_id>', views.task_toggle, name='task-toggle'),
    path('task-view/<str:task_id>/', views.task_view, name='task-view'),
    #path('connect-employee/<str:task_id>/<str:employee_id>/', views.connect_employee, name='connect-employee'),

    path('employee-list', views.employee_list, name='employee-list'),
    path('employee-create', views.employee_create, name='employee-create'),
    path('employee-update/<str:employee_id>', views.employee_update, name='employee-update'),
    path('employee-delete/<str:employee_id>', views.employee_delete, name='employee-delete'),
]
