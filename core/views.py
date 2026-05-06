from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Project, Task
from .forms import CustomUserCreationForm, ProjectForm, TaskForm, TaskStatusUpdateForm

def is_admin(user):
    return user.is_authenticated and user.role == 'Admin'

class AdminRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.role == 'Admin'

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user
    if user.role == 'Admin':
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(assigned_to=user)
    
    total = tasks.count()
    pending = tasks.filter(status='Pending').count()
    in_progress = tasks.filter(status='In Progress').count()
    completed = tasks.filter(status='Completed').count()
    overdue = tasks.filter(status='Overdue').count()

    context = {
        'tasks': tasks,
        'total': total,
        'pending': pending,
        'in_progress': in_progress,
        'completed': completed,
        'overdue': overdue,
    }
    return render(request, 'dashboard.html', context)

class ProjectCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'create_project.html'
    success_url = reverse_lazy('dashboard')

class TaskCreateView(LoginRequiredMixin, AdminRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'create_task.html'
    success_url = reverse_lazy('dashboard')

class TaskUpdateStatusView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskStatusUpdateForm
    template_name = 'update_task_status.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        qs = super().get_queryset()
        if self.request.user.role == 'Admin':
            return qs
        return qs.filter(assigned_to=self.request.user)

@login_required
@user_passes_test(is_admin)
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete_task.html', {'task': task})

