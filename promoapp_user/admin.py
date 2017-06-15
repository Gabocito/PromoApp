from django.contrib import admin

from promoapp_user.models import User, StoreManager, PromotionManager, Admin

admin.site.register(User)

admin.site.register(StoreManager)

admin.site.register(PromotionManager)

admin.site.register(Admin)

