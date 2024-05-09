from django.contrib import admin

from .models import Booking, BookingService, Guest, Hotel, HotelComment, HotelService, Profile, Room

admin.site.register(Guest)
admin.site.register(Profile)
admin.site.register(Hotel)
admin.site.register(Room)
admin.site.register(HotelComment)
admin.site.register(Booking)
admin.site.register(HotelService)
admin.site.register(BookingService)
