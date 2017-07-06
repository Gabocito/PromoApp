from rest_framework import permissions
from models import Admin

class isAdmin(permissions.BasePermission):
    """
    Custom Permission to only allow Admins to manage user objects.
    """
    def has_permission(self, request, view):
        if Admin.objects.filter(user_id=request.user.pk):
            return True
        return False

class isCurrentUserOrAdmin(permissions.BasePermission):
    """
    Custom Permission to only allow Users to manage their own user data.
    """
    def has_object_permission(self, request, view, obj):
        if (Admin.objects.filter(user_id=request.user.pk) or request.user == obj.user):
            return True
        return False

class isCurrentUserAndAdmin(permissions.BasePermission):
    """
    Custom Permission to only allow Users to manage their own user data.
    """
    def has_object_permission(self, request, view, obj):
        if (Admin.objects.filter(user_id=request.user.pk) and request.user == obj.user):
            return True
        return False