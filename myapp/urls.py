from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('create_service_request/', views.create_service_request, name='create_service_request'),
    path('service_request_success/', views.service_request_success, name='service_request_success'),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)