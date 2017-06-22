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
    url(r'^stores/(?P<pk>[0-9]+)/$', StoreView.as_view(), name='store'),
    url(r'^stores/(?P<pk>[0-9]+)/edit/$', StoreFormEdit.as_view(), name='store-edit'),
]