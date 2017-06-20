from django.conf.urls import url

from views import *

urlpatterns = [
    # **********************   CREATE/LIST ***********************
    url(r'^promotions/$', PromotionListCreate.as_view(), name='promotions'),
    url(r'^promotions/new/$', PromotionFormCreate.as_view(), name='promotions-new'),
    url(r'^advertisingcampaigns/$', AdvertisingCampaignListCreate.as_view(), name='advertisingcampaigns'),
    url(r'^advertisingcampaigns/new/$', AdvertisingCampaignFormCreate.as_view(), name='advertisingcampaigns-new'),
    url(r'^companies/$', CompanyListCreate.as_view(), name='companies'),
    url(r'^companies/new/$', CompanyFormCreate.as_view(), name='companies-new'),
    url(r'^stores/$', StoreListCreate.as_view(), name='stores'),
    url(r'^stores/new/$', StoreFormCreate.as_view(), name='stores-new'),
    # ****************   DETAILS/UPDATE/DELETE *******************
    url(r'^promotions/(?P<pk>[0-9]+)/$', PromotionView.as_view(), name='promotion'),
    url(r'^promotions/(?P<pk>[0-9]+)/edit/$', PromotionFormEdit.as_view(), name='promotion-edit'),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/$', AdvertisingCampaignView.as_view(), name='advertisingcampaign'),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/edit/$', AdvertisingCampaignFormEdit.as_view(), name='advertisingcampaign-edit'),
    url(r'^companies/(?P<pk>[0-9]+)/$', CompanyView.as_view(), name='company'),
    url(r'^companies/(?P<pk>[0-9]+)/edit/$', CompanyFormEdit.as_view(), name='company-edit'),
    url(r'^stores/(?P<pk>[0-9]+)/$', StoreView.as_view(), name='store'),
    url(r'^stores/(?P<pk>[0-9]+)/edit/$', StoreFormEdit.as_view(), name='store-edit'),
]