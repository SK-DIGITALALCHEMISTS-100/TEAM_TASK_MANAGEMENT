from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import User, Project, Task
from .serializers import UserSerializer, ProjectSerializer, TaskSerializer

class IsAdminUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.role == 'Admin')

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated(), IsAdminUser()]
        return [permissions.IsAuthenticated()]

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'Admin':
            return Task.objects.all()
        return Task.objects.filter(assigned_to=user)

    def get_permissions(self):
        if self.action in ['create', 'destroy']:
            return [permissions.IsAuthenticated(), IsAdminUser()]
        return [permissions.IsAuthenticated()]

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def dashboard_stats(request):
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

    return Response({
        'total': total,
        'pending': pending,
        'in_progress': in_progress,
        'completed': completed,
        'overdue': overdue
    })
