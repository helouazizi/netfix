from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('register/customer/', views.register_customer, name='register_customer'),
    path('register/company/', views.register_company, name='register_company'),
]