from django.urls import path
from .views import home_view, hotel_view, hotels_view, users_view


urlpatterns = [
    path('', home_view, name='Home'),
    path('hotels', hotels_view, name='Hotels'),
    path('hotels/<str:hotel_name>', hotel_view, name='Hotel'),
    path('users', users_view, name='Users'),

    # re_path(r"^articles/(?P<year>[0-9]{4})/$", views.year_archive),
]
