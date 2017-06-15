from django.conf.urls import url

from views import *

urlpatterns = [
    # **********************   CREATE/LIST ***********************
    url(r'^promotions', PromotionListCreate.as_view()),
    url(r'^advertisingcampaigns', AdvertisingCampaignListCreate.as_view()),
    url(r'^companies', CompanyListCreate.as_view()),
    url(r'^stores', StoreListCreate.as_view()),
    # ****************   DETAILS/UPDATE/DELETE *******************
    url(r'^promotions/(?P<pk>[0-9]+)/$', Promotion.as_view()),
    url(r'^advertisingcampaigns/(?P<pk>[0-9]+)/$', AdvertisingCampaign.as_view()),
    url(r'^companies/(?P<pk>[0-9]+)/$', Company.as_view()),
    url(r'^stores/(?P<pk>[0-9]+)/$', Store.as_view()),
]