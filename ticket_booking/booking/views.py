from django.shortcuts import render, get_object_or_404
from .models import Event
from django.http import JsonResponse

def events(request):
    events = Event.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'booking/events.html', context)

def book_ticket(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    # Logic for booking the ticket would go here
    return JsonResponse({'message': 'Tickets booked for ' + event.name})

def index(request):
    events = Event.objects.all()
    return render(request, 'booking/index.html', {'events': events})

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
