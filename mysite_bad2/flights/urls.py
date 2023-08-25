from django.urls import path
from .views import hello, airports, flight, date_filter

app_name = 'flight'
urlpatterns = [
    # path('hello', hello),
    path('', airports, name='airports'),
    path('<int:flight_id>', flight, name='flight'),
    path('date-filter/', date_filter, name='date_filter')
]