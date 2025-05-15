from django.urls import path
from . import views

urlpatterns = [
    path('',views.servives,name='services'),
    path('create/', views.create_service, name='create_service'),
    path('profile/', views.profile_view, name='profile'),
    # Service detail page
    path('<int:service_id>/', views.service_detail, name='service_detail'),

    # Request service (can be a POST endpoint)
    path('<int:service_id>/request/', views.request_service, name='request_service'),
]