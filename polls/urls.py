from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [

    url(r'^temp/$', views.getdata, name = 'getdata'),

    url(r'^water/$', views.getdata, name='getdata'),

    url(r'^soil/$', views.getdata, name='getdata'),

    url(r'^$', views.index, name='index'),
]
