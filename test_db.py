import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager.settings')
django.setup()

from core.models import User, Project, Task

print("Users:", User.objects.all())
print("Projects:", Project.objects.all())
print("Tasks:", Task.objects.all())
