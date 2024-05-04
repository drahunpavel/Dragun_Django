from django.urls import path
# from django.views.defaults import page_not_found
from .views import home_template_view, hotel_template_view, hotels_template_view, not_found_template_view, users_template_view

# from django.conf.urls import handler404

# handler404 = 'booking_service/404.html'

urlpatterns = [
    path('', home_template_view, name = 'Home'),
    path('hotels', hotels_template_view, name = 'Hotels'),
    path('hotels/<str:hotel_name>', hotel_template_view, name = 'Hotel'),
    path('users', users_template_view, name = 'Users'),
    # re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
]
