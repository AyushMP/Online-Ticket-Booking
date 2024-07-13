from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Maps to the root URL '/'
    path('events/', views.events, name='events'),  # Maps to '/events/'
    path('about/', views.about, name='about'),  # Maps to '/about/'
    path('other/', views.other_templates, name='other_templates'),  # Maps to '/other/'
    path('home/', views.home, name='home'),  # Example: Maps to '/home/'
]
