from django.urls import path, include

from rest_framework.routers import DefaultRouter

from ..views import user_views


app_name = 'users'

router = DefaultRouter()
router.register('users', user_views.UserViewSet, basename='client_users')
router.register('admins', user_views.AdminUserViewSet, basename='admin_users')

urlpatterns = (
    path('',include(router.urls)),
)