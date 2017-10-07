from django.conf.urls import url
from . import views

app_name = 'users'

urlpatterns = [url(r'^signup/', views.signup, name='signup'),
               url(r'^login/', views.login, name='login'),
               url(r'^logout/', views.logout, name='logout'),
               url(r'^makeUser/', views.makeUser, name='makeUser'),
               url(r'^profile/', views.profile, name="profile"),
               url(r'^UserProfile/', views.UserProfile, name='UserProfile'),
               url(r'^tutorial/', views.tutorial, name="tutorial"),
               url(r'^graph/', views.graph, name="graph"),
               url(r'^sensors/', views.sensors, name="sensors"),
               url(r'^weather/', views.weather, name="weather"),
               url(r'^contact/', views.contact, name="contact"),
               url(r'^water/',views.water, name="water"),]
