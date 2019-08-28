from django.urls import path
from newapp import views 
urlpatterns = [
 path('', views.index), 
 path('register', views.register),
 path('login', views.login),
 path('travels', views.travels),
 path('addtrip', views.addtrip),
 path('create_trip', views.create_trip),
 path('showtravels/<trip_id>', views.showtravels),
 path('logout', views.logout),
 path('jointravels/<trip_id>', views.jointravels),


]
