from django.urls import path
from . import views

urlpatterns = [
    path('',views.servives,name='services'),
    path('create/', views.create_service, name='create_service'),
]