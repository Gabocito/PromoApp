from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^index/$', Index.as_view(), name='index'),
    # **********************   CREATE/LIST ***********************
    url(r'^users/$', UserListCreate.as_view(), name='users'),
    url(r'^storemanagers/new/$', StoreManagerFormCreate.as_view(), name='storemanagers-new'),
    url(r'^storemanagers/$', StoreManagerListCreate.as_view(), name='storemanagers'),
    url(r'^promotionmanagers/new/$', PromotionManagerFormCreate.as_view(), name='promotionmanagers-new'),
    url(r'^promotionmanagers/$', PromotionManagerListCreate.as_view(), name='promotionmanagers'),
    url(r'^admins/$', AdminListCreate.as_view(), name='admins'),
    # ****************   DETAILS/UPDATE/DELETE *******************
    url(r'^users/(?P<pk>[0-9]+)/$', UserView.as_view(), name='user'),
    url(r'^storemanagers/(?P<pk>[0-9]+)/$', StoreManagerView.as_view(), name='storemanager'),
    url(r'^promotionmanagers/(?P<pk>[0-9]+)/$', PromotionManagerView.as_view(), name='promotionmanager'),
    url(r'^admins/(?P<pk>[0-9]+)/$', AdminView.as_view(), name='admin'),
]