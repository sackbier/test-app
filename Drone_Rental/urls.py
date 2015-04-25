from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^drone-index/$', views.DroneIndex.as_view(), name='drone-index'),
    url(r'^detail/(?P<pk>\d+)/$', views.CaseDetailView.as_view(), name='detail'),
    url(r'^drone/(?P<pk>\d+)/$', views.DroneDetailView.as_view(), name='drone_detail'),
    url(r'^drone/(?P<current_drone>\d+)/edit/$', views.edit_drone, name='drone_edit'),
    url(r'^customer/(?P<pk>\d+)/$', views.CustomerDetailView.as_view(), name='customer_detail'),
]