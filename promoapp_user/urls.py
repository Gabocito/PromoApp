from django.conf.urls import url

from views import *

urlpatterns = [
    url(r'^index', Index.as_view()),
    # **********************   CREATE/LIST ***********************
    url(r'^users', UserListCreate.as_view()),
    url(r'^storemanagers', StoreManagerListCreate.as_view()),
    url(r'^promotionmanagers', PromotionManagerListCreate.as_view()),
    url(r'^admins', AdminListCreate.as_view()),
    # ****************   DETAILS/UPDATE/DELETE *******************
    url(r'^users/(?P<pk>[0-9]+)/$', UserView.as_view()),
    url(r'^storemanagers/(?P<pk>[0-9]+)/$', StoreManagerView.as_view()),
    url(r'^promotionmanagers/(?P<pk>[0-9]+)/$', PromotionManagerView.as_view()),
    url(r'^admins/(?P<pk>[0-9]+)/$', AdminView.as_view()),
]