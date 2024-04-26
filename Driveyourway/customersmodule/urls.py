from django.urls import path
from . import views

urlpatterns = [
    # Your URL patterns go here
    path('Home', views.Customerhome , name='customeromepage'),
    path('viewallbookings',views.Viewallbookings,name='viewallbookings'),
    path('feedback',views.feedback,name='feedback'),
    path('logout', views.logout, name='logout'),

]
