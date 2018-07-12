from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
        url(r'^$', views.index),
        url(r'^login/$', login, {'template_name': 'hotel/login.html'}, name='login'),
        url(r'^search/$', views.search, name='search'),
]
