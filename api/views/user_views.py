from rest_framework import viewsets

from ..serializers.user_serializers import UserSerializer, AdminUserSerializer
from ..models.users import User
from ..permissions import user_permissions

class UserViewSet(viewsets.ModelViewSet):
    """API View for client users"""

    permission_classes = (user_permissions.IsOwner,)
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_superuser=False)


class AdminUserViewSet(viewsets.ModelViewSet):
    """API View for admin users"""

    permission_classes = (user_permissions.IsOwner,) 
    serializer_class = AdminUserSerializer
    queryset = User.objects.filter(is_superuser=True)
