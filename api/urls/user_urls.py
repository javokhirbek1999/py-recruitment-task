from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ..views.user_views import UserViewSet, AdminUserViewSet


app_name = 'users'

router = DefaultRouter()
router.register('users', UserViewSet, basename='client-users')
router.register('admins', AdminUserViewSet, basename='admin-users')

urlpatterns = (
    path('',include(router.urls)),
)