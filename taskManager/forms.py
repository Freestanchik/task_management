from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(max_length=100)
    additional_info = forms.CharField(max_length=100)
    priority = forms.IntegerField(min_value=1, max_value=5)


class WorkerForm(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    role = forms.CharField(max_length=100)