from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_user, me, UserViewSet, ProjectViewSet, TaskViewSet, dashboard_stats

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('auth/register/', register_user, name='register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/me/', me, name='me'),
    path('dashboard/', dashboard_stats, name='dashboard_stats'),
    path('', include(router.urls)),
]
