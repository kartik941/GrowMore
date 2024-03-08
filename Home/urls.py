
from django.urls import path
import views
urlpatterns = [
    path('', views.home),
    path('home', views.home),
]