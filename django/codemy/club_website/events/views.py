from django.shortcuts import render, redirect
from django.contrib import messages
import calendar
from django.http import HttpResponseRedirect
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.http import HttpResponse
from django.core.paginator import Paginator


def venue_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment;filename=venues.txt'

    venues = Venue.objects.all()
    lines = []
    for venue in venues:
        lines.append(f'{venue.name}\n')
        lines.append(f'{venue.address}\n')
        lines.append(f'{venue.phone}\n\n\n')
    response.writelines(lines)

    return response


# Create your views here.
def show_events(request):
    event_list = Event.objects.all().order_by('event_date')

    context = {
        'event_list': event_list
    }
    return render(request, 'events/event_list.html', context=context)


def add_event(request, submitted=False):
    submitted = False
    if request.POST:
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('?submitted=True')
        else:
            pass
    form = EventForm
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'events/add_event.html', {"form": form, "submitted": submitted})


def update_event(request, pk):
    event = Event.objects.get(pk=pk)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
        form.save()
        return redirect('events:list-events')
    return render(request, 'events/update_event.html', {'event': event, 'form': form})


def delete_event(request, pk):
    event = Event.objects.get(pk=pk)
    event.delete()
    return redirect('events:list-events')


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html', {'form': form, 'submitted': submitted})


def list_venues(request):
    venue_list = Venue.objects.all()
    p = Paginator(Venue.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)
    num_pages = range(1, venues.paginator.num_pages + 1)
    return render(request, 'events/venues.html',
                  {'venue_list': venue_list, 'venues': venues, 'num_pages': num_pages, 'page_num': page})


def show_venue(request, pk):
    venue = Venue.objects.get(pk=pk)
    return render(request, 'events/venue_detail.html', {'venue': venue})


def update_venue(request, pk):
    venue = Venue.objects.get(pk=pk)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
        form.save()
        return redirect('events:list-venues')
    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})


def delete_venue(request, pk):
    event = Venue.objects.get(pk=pk)
    event.delete()
    return redirect('events:list-venues')


def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, 'events/search_venues.html', {'searched': searched, 'venues': venues})
    return render(request, 'events/search_venues.html')


def home(request, year=datetime.now().year, month=datetime.now().strftime("%B")):
    month = month.capitalize()
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    current_year = now.year
    time = now.strftime('%I:%M:%S %p')

    context = {
        "year": year,
        "month": month,
        "month_number": month_number,
        "current_year": current_year,
        "time": time,
        "cal": cal,
    }
    return render(request, 'events/home.html', context)
