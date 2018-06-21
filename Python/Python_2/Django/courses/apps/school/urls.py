from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'add/$',views.add),
    url(r'destroy/(?P<id>\d+)/$', views.destroy),
    url(r'(?P<id>\d+)/process/$',views.process),
    url(r'(?P<id>\d+)/comments/$',views.comments),
    url(r'(?P<id>\d+)/comments/add_comment/$',views.add_comment),
]