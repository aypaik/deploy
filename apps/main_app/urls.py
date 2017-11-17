from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^add/?$', views.add),
    url(r'^create/?$', views.create),
    url(r'^show/?(?P<user_id>\d+)$', views.show),
    url(r'^edit/?(?P<user_id>\d+)$', views.edit),
    url(r'^update/?(?P<user_id>\d+)$', views.update),
    url(r'^delete/?(?P<user_id>\d+)$', views.delete),


]
