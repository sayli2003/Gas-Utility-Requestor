from django.urls import path
from . import views

urlpatterns = [
    path('create_service_request/', views.create_service_request, name='create_service_request'),
    path('service_request_success/', views.service_request_success, name='service_request_success'),
]