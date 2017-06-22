from django.conf.urls import url

from views import *

urlpatterns = [
    # **********************   CREATE/LIST ***********************
    url(r'^promotions/$', PromotionListCreate.as_view(), name='promotions'),
    url(r'^promotions/add/$', PromotionFormCreate.as_view(), name='promotions-add'),
    url(r'^advertisingcampaigns/$', AdvertisingCampaignListCreate.as_view(), name='advertisingcampaigns'),
    url(r'^advertisingcampaigns/add/$', AdvertisingCampaignFormCreate.as_view(), name='advertisingcampaigns-add'),
    # ****************   DETAILS/UPDATE/DELETE *******************
    url(r'^promotions/(?P<pk>[0-9]+)/$', PromotionView.as_view(), name='promotion'),
    url(r'^promotions/(?P<pk>[0-9]+)/edit/$', PromotionFormEdit.as_view(), name='promotion-edit'),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/$', AdvertisingCampaignView.as_view(), name='advertisingcampaign'),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/edit/$', AdvertisingCampaignFormEdit.as_view(), name='advertisingcampaign-edit'),
]