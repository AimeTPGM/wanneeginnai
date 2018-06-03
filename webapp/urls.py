from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^add$', views.add, name='add'),
    url(r'^list$', views.listpage, name='listpage'),
    url(r'^random$', views.random, name='random'),
]