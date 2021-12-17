from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwner(BasePermission):
    """Permission class for controlling access for users to perform CRUD operations"""

    def has_object_permission(self, request, view, obj):
        """Rectrict users to perform CRUD operations on other users' account"""

        if request.method in SAFE_METHODS:
            return True
        
        return request.user.id == obj.id