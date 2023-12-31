from django.contrib import admin
from .models import Flight, Airport, Passenger, Security

# Register your models here.
admin.site.register(Flight)
#admin.site.register(Passenger)


class FlightInline(admin.TabularInline):
    model = Flight
    fk_name = 'origin'
    extra = 10

@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    inlines = [FlightInline, ]
@admin.register(Passenger)
class AirportAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':('name', 'second_name')
    }
@admin.register(Security)
class AirportAdmin(admin.ModelAdmin):
    list_display = ('name', 'second_name', 'post')