from django.conf.urls import url

from views import *

urlpatterns = [
    # **********************   CREATE/LIST ***********************
    url(r'^companies/$', CompanyListCreate.as_view(), name='companies'),
    url(r'^companies/add/$', CompanyFormCreate.as_view(), name='companies-add'),
    url(r'^stores/$', StoreListCreate.as_view(), name='stores'),
    url(r'^stores/add/$', StoreFormCreate.as_view(), name='stores-add'),
    # ****************   DETAILS/UPDATE/DELETE *******************
    url(r'^companies/(?P<pk>[0-9]+)/$', CompanyView.as_view(), name='company'),
    url(r'^companies/(?P<pk>[0-9]+)/edit/$', CompanyFormEdit.as_view(), name='company-edit'),
    url(r'^companies/(?P<pk>[0-9]+)/edit/status/$', CompanyEditStatus.as_view(), name='company-edit-status'),
    url(r'^stores/(?P<pk>[0-9]+)/company/$', CompanyDelete.as_view(), name='company-delete'),
    url(r'^stores/(?P<pk>[0-9]+)/$', StoreView.as_view(), name='store'),
    url(r'^stores/(?P<pk>[0-9]+)/edit/$', StoreFormEdit.as_view(), name='store-edit'),
    url(r'^stores/(?P<pk>[0-9]+)/edit/status/$', StoreEditStatus.as_view(), name='store-edit-status'),
    url(r'^stores/(?P<pk>[0-9]+)/delete/$', StoreDelete.as_view(), name='store-delete'),
    url(r'^stores/(?P<pk>[0-9]+)/remove/advertisingcampaign/(?P<advertisingcampaign>[0-9]+)/$', StoreRemoveAdvertisingCampaign.as_view(), name='store-remove-advertisingcampaign'),
]