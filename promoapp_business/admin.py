from django.contrib import admin

from promoapp_business.models import Promotion, AdvertisingCampaign, Company, Store

admin.site.register(Promotion)

admin.site.register(AdvertisingCampaign)

admin.site.register(Company)

admin.site.register(Store)