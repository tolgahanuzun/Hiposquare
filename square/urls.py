from django.conf.urls import url
from square import views

urlpatterns = [

    url(r'^search/$', views.search),
    url(r'^$', views.base),
]

