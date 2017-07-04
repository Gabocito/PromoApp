from rest_framework import permissions
from promoapp_user.models import Admin, PromotionManager

class isAdminOrPromotionManager(permissions.BasePermission):
    """
    Custom Permission to only allow Admins or Promotion Managers to access the Promotions section.
    """
    def has_permission(self, request, view):
        if Admin.objects.filter(user_id=request.user.pk) or PromotionManager.objects.filter(user_id=request.user.pk):
            return True
        return False