from django.urls import path

from .views import home_view, places_view

urlpatterns = [
    path('', home_view, name = 'Home'),
    path('places', places_view, name = 'Places')
]
