from django.conf.urls import url

from views import *

urlpatterns = [
    # **********************  EDIT/PROFILE  **********************
    url(r'^profile/$', Profile.as_view(), name='profile'),
    # **********************  LOGIN/LOGOUT  **********************
    url(r'^login/$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    # **********************   DASHBOARD   ***********************
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
    # **********************   CREATE/LIST ***********************
    url(r'^users/$', UserListCreate.as_view(), name='users'),
    url(r'^storemanagers/add/$', StoreManagerFormCreate.as_view(), name='storemanagers-add'),
    url(r'^storemanagers/$', StoreManagerListCreate.as_view(), name='storemanagers'),
    url(r'^promotionmanagers/add/$', PromotionManagerFormCreate.as_view(), name='promotionmanagers-add'),
    url(r'^promotionmanagers/$', PromotionManagerListCreate.as_view(), name='promotionmanagers'),
    url(r'^admins/$', AdminListCreate.as_view(), name='admins'),
    # ****************   DETAILS/UPDATE/DELETE *******************
    url(r'^users/(?P<pk>[0-9]+)/$', UserView.as_view(), name='user'),
    url(r'^storemanagers/(?P<pk>[0-9]+)/$', StoreManagerView.as_view(), name='storemanager'),
    url(r'^storemanagers/(?P<pk>[0-9]+)/edit/$', StoreManagerFormEdit.as_view(), name='storemanager-edit'),
    url(r'^storemanagers/(?P<pk>[0-9]+)/edit/status/$', StoreManagerEditStatus.as_view(), name='storemanager-edit-status'),
    url(r'^storemanagers/(?P<pk>[0-9]+)/delete/$', StoreManagerDelete.as_view(), name='storemanager-delete'),
    url(r'^promotionmanagers/(?P<pk>[0-9]+)/$', PromotionManagerView.as_view(), name='promotionmanager'),
    url(r'^promotionmanagers/(?P<pk>[0-9]+)/edit/$', PromotionManagerFormEdit.as_view(), name='promotionmanager-edit'),
    url(r'^promotionmanagers/(?P<pk>[0-9]+)/edit/status/$', PromotionManagerEditStatus.as_view(), name='promotionmanager-edit-status'),
    url(r'^promotionmanagers/(?P<pk>[0-9]+)/delete/$', PromotionManagerDelete.as_view(), name='promotionmanager-delete'),
    url(r'^admins/(?P<pk>[0-9]+)/$', AdminView.as_view(), name='admin'),
]