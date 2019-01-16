from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('arrivals.html', views.arrivals, name='arrivals'),
    path('departures.html', views.departures, name='departures'),
    path('adminpanel', views.adminpanel, name='adminpanel'),
    path('addarrival', views.addarrival, name='addarrival'),
    path('deletearrival', views.deletearrival, name='deletearrival'),
    path('adddeparture', views.adddeparture, name='adddeparture'),
    path('deletedeparture', views.deletedeparture, name='deletedeparture'),
    path('error.html', views.error, name='error'),
 ]
