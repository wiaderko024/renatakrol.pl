from django.shortcuts import render
from django.utils import timezone
from .models import Event


def all_events_page(request):
    all_events = Event.objects.all()
    events = []
    old_events = []
    today = timezone.now()

    for e in all_events:
        if today.isoformat() <= e.time.isoformat():
            events.append(e)
        else:
            old_events.append(e)

    old_events.reverse()
    events.reverse()

    context = {
        'old_events': old_events,
        'events': events
    }

    return render(request, 'events.html', context=context)


def event_page(request, id):
    event = Event.objects.get(pk=id)
    return render(request, 'event.html', {'event': event})
