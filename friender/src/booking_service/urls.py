from django.urls import path
from .views import home_template_view, hotel_template_view, hotels_template_view, users_template_view


urlpatterns = [
    path('', home_template_view, name = 'Home'),
    path('hotels', hotels_template_view, name = 'Hotels'),
    path('hotels/<str:hotel_name>', hotel_template_view, name = 'Hotel'),
    path('users', users_template_view, name = 'Users'),

    # re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
]
