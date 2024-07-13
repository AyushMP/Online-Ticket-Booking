from django.shortcuts import render
from .models import Event

def index(request):
    events = Event.objects.all()
    return render(request, 'booking/index.html', {'events': events})

def events(request):
    events = Event.objects.all()  # Retrieve all events
    context = {
        'events': events,
    }
    return render(request, 'booking/events.html', context)

def other_templates(request):
    return render(request, 'booking/other_templates.html')

def about(request):
    return render(request, 'booking/about.html')

def home(request):
    # Example context data
    context = {
        'title': 'Welcome to My Booking App',
        'content': 'This is the home page content.',
        'items': ['item1', 'item2', 'item3'],
    }
    return render(request, 'booking/home.html', context)
