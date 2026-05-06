from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Project, Task

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('role',)

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project', 'assigned_to', 'due_date']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})
        }

class TaskStatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status']
