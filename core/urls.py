from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    path('', views.dashboard, name='dashboard'),
    path('projects/create/', views.ProjectCreateView.as_view(), name='create_project'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='create_task'),
    path('tasks/<int:pk>/update-status/', views.TaskUpdateStatusView.as_view(), name='update_task_status'),
    path('tasks/<int:pk>/delete/', views.delete_task, name='delete_task'),
]
