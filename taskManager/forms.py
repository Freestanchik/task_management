from django import forms

from taskManager.models import Employee


class TaskForm(forms.Form):
    name = forms.CharField(max_length=100)
    additional_info = forms.CharField(max_length=1000)
    priority = forms.IntegerField(min_value=1, max_value=5)
    role = forms.ChoiceField(choices=[('frontend', 'Frontend'), ('backend', 'Backend'), ('management', 'Management')])


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    role = forms.ChoiceField(choices=[('frontend', 'Frontend'), ('backend', 'Backend'), ('management', 'Management')])


class TaskAssignmentForm(forms.Form):
    employee = forms.ModelChoiceField(
        queryset=Employee.objects.all(),
        empty_label="Select an Employee",
        label="Assigned Employee",
        to_field_name='id',  # Specify the field used as the value of the <option> elements
    )
