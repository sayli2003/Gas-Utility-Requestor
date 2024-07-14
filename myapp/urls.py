from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('create_service_request/', views.create_service_request, name='create_service_request'),
    path('service_request_success/', views.service_request_success, name='service_request_success'),

]
