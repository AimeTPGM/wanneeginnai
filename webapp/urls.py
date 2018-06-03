from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.random, name='random'),
    url(r'^add$', views.add, name='add'),
    url(r'^list$', views.listpage, name='listpage'),
]