from django.urls import path, include
from . import views
from .views import index 

urlpatterns = [
    path('', views.index, name='index'),
    path('clear/', views.clear_recent, name='clear_recent'),
   
]
