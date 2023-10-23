from django.contrib import admin
from .models import Car,Booking,CarType
# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
 list_display = ['c_name', 'c_price', 'c_model', 'c_type', 'c_status']
 list_filter = ['c_status', 'c_model', 'c_type']
 search_fields = ['c_name', 'c_type']
 prepopulated_fields = {'c_slug':('c_name',)}

admin.site.register(Booking)

admin.site.register(CarType)
