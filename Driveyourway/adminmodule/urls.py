from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('checkadminlogin/', views.login, name="checkadminlogin"),
    path('Home/', views.home, name="home"),
    path("checkregistration/", views.checkregistration, name="checkregistration"),
    path("Viewallcustomers/",views.viewallcustomers,name="viewallcustomers"),
    path("carbooking", views.carbooking, name='carbooking'),
    path("payment", views.payment, name='payment'),
    path("cardriverbooking", views.cardriverbooking, name='cardriverbooking'),
    path("carservices", views.carservices, name='carservices'),
    path('calculator', views.calculator, name='calculator'),
    path("confirm", views.confirm, name='confirm'),

]