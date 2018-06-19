from django.conf.urls import url
from . import views           # This line is new!copy
urlpatterns = [
    url(r'^$', views.index),
    url(r'(?P<number>\d+)$',views.show),
    url(r'(?P<number>\d+)/edit$',views.edit),
    url(r'^delete/$',views.destroy),
    url(r'^new/$',views.new),
    url(r'^create/$',views.create),
  ]