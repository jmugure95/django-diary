from django.urls import path
from . import views

app_name = 'entry'

urlpatterns = [
    path('',views.home_view,name="home" ),
    path('entry/',views.entry_view,name="entr"),
]
