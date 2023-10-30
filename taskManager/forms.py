from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(max_length=100)
    additional_info = forms.CharField(max_length=100)
    priority = forms.IntegerField(min_value=1, max_value=5)
    role = forms.ChoiceField(choices=[('frontend', 'Frontend'), ('backend', 'Backend'), ('management', 'Management')])

class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    role = forms.ChoiceField(choices=[('frontend', 'Frontend'), ('backend', 'Backend'), ('management', 'Management')])