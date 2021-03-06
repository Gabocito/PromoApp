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
    url(r'^promotions/(?P<pk>[0-9]+)/edit/status/$', PromotionEditStatus.as_view(), name='promotion-edit-status'),
    url(r'^promotions/(?P<pk>[0-9]+)/delete/$', PromotionDelete.as_view(), name='promotion-delete'),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/$', AdvertisingCampaignView.as_view(), name='advertisingcampaign'),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/edit/$', AdvertisingCampaignFormEdit.as_view(), name='advertisingcampaign-edit'),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/edit/status/$', AdvertisingCampaignEditStatus.as_view(), name='advertisingcampaign-edit-status'),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/remove/promotion/(?P<promotion>[0-9]+)/$', AdvertisingCampaignRemovePromotion.as_view(), name='advertisingcampaign-remove-promotion'),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/delete/$', AdvertisingCampaignDelete.as_view(), name='advertisingcampaign-delete'),
]