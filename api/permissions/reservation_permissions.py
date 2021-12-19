from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsReservationOwner(BasePermission):
    """Permission class to control access for reservation"""

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        return request.user.id == obj.client.id