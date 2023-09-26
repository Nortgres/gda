from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Flight, Airport, Passenger, Security


# Create your views here.
def hello(request):
    #all_objs = Flight.objects.all()     #[1:3] можно сделать срез
    #first_objs = Flight.objects.first()
    #print(first_objs)
    #ordered_obj = Flight.objects.order_by('duration') #можно сделать с минусом для обратной сортировки
    #ordered_obj = Flight.objects.order_by('-duration').first()
    #print(ordered_obj)
    #get_obj = Flight.objects.get(id=1)

    #my_airport = Airport.objects.get(name='Пулково')
    #get_airports_flights = Flight.objects.filter(destination=my_airport)# или использовать id
    #print(get_airports_flights)

    #get_exclude_airports = Flight.objects.filter(origin=2).exclude(destination=1)
    #print(get_exclude_airports)

    #my_airport1 = Airport.objects.get(name='Пулково')
    #my_airport2 = Airport.objects.get(name='Хитроу')
    #f = Flight.objects.create(origin=my_airport1, destination=my_airport2, duration=2)
    #print(f)

    #f = Flight.objects.get(id=1)
    #f.duration = 200
    #f.save()
    #print(f)

    #Flight.objects.get(id=1).delete()
    """Airport.objects.bulk_create([
        Airport(name='Иваново', city='Иваново'),
        Airport(name='Внуково', city='Москва')
    ])"""
    #print(Airport.objects.get_or_create(name='Иваново', city='Иваново'))

    ##my_airport = Airport.objects.get(name='Шереметьево')
    ##get_airports_flight = Flight.objects.filter(origin=my_airport)
    ##print(get_airports_flight)
    ##get_passenger = Passenger.objects.filter(flights=get_airports_flight)


#    my_airport = Airport.objects.get(name='Шереметьево')
#    res = Passenger.objects.filter(flights__origin=my_airport)
#    print(res)
#    return HttpResponse('success')

#   my_airport = Airport.objects.get(name='Шереметьево')
#   res = Passenger.objects.filter(flights__origin=my_airport)[:3]
#    return HttpResponse(res)

    return HttpResponse('success')

def airports(request):
    f = Airport.objects.all()
    context = {
        'airports': f
    }
    return render(request, 'index.html', context)


def flight(request, flight_id):
    # f = Flight.objects.get(pk=flight_id)
    f = get_object_or_404(Flight, pk=flight_id)
    context = {
        'flight': f
    }
    #print(f.passanger_flights.all())
    #print(dir(f))
    return render(request, 'flight.html', context)

def date_filter(request):
    start_date = request.GET.get('start_date')
    filter_type = request.GET.get('filter_type')
    f = None
    if start_date:
        if filter_type == 'gte':
            f = Flight.objects.filter(created__gte = start_date)
        elif filter_type == 'lte':
            f = Flight.objects.filter(created__lte=start_date)
    context = {
        'flights': f,
        'date': start_date
    }
    return render(request, 'date_filter.html', context)

def passanger(request, slug):
    p = Passenger.objects.get(slug=slug)

    context = {
        'passanger' : p
    }
    return HttpResponse(p)

def security(request, slug):
    p = Security.objects.get(slug=slug)

    context = {
        'security' : p
    }
    return HttpResponse(p)