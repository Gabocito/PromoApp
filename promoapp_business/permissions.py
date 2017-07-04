from rest_framework import permissions
from promoapp_user.models import Admin, StoreManager

class isAdminOrStoreManager(permissions.BasePermission):
    """
    Custom Permission to only allow Admins or Store Managers to access the Business section.
    """
    def has_permission(self, request, view):
        if Admin.objects.filter(user_id=request.user.pk) or StoreManager.objects.filter(user_id=request.user.pk):
            return True
        return False
