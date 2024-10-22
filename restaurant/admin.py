from django.contrib import admin
from .models import MenuItem, Booking

# Register your models here.

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'price','description', 'inventory']
    search_fields = ['title']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email','phone_number', 'booking_date', 'number_of_people', 'special_requests', 'created_at', 'updated_at']
    search_fields = ['customer_name']
    list_filter = ['booking_date']