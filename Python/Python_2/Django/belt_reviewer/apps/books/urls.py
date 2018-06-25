from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index),
    url(r'books/$',views.dashboard),
    url(r'books/add/$',views.add),
    url(r'books/(?P<id>\d+)$',views.books),
    url(r'users/(?P<id>\d+)$',views.users),
    url(r'process/$',views.process),
    url(r'logout/$',views.logout)
]