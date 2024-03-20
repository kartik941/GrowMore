
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home),
    path('home', views.home),
    path('about', views.about),
    path('market', views.market),
    path('charts', views.charts),
    path('news', views.news),
    path('Analyse', views.analyse),
    path('login', views.login), 
    path('login1', views.login1), 
    path('login2', views.login2), 
    path('tutorial', views.tutorial), 
]