from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('booking.urls')),  # Direct root URL to booking app URLs
    path('admin/', admin.site.urls),
    path('booking/', include('booking.urls')),
    
]
