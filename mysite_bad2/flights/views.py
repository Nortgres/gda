from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Flight, Airport


# Create your views here.
def hello(request):
    return HttpResponse('hello')


def airports(request):
    f = Airport.objects.all()
    context = {
        'airports': f
    }
    return render(request, 'index.html', context)


def flight(request, flight_id):
    #f = Flight.objects.get(pk=flight_id)
    f = get_object_or_404(Flight, pk=flight_id)
    context = {
        'flight': f
    }
    return render(request, 'flight.html', context)

def date_filter(request):
    start_date = request.GET.get('start_date')
    f = None
    if start_date:
        f = Flight.object.filter(created__gte = start_date)
    contex = {
        'flights': f,
        'date': start_date
    }
    return render(request, 'date_filter.html', context)