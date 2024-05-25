from django.urls import URLPattern, include, path

from .views import GuestApiView, HotelServiceApiView, hello_world


guests_patterns: list[URLPattern] = [
    path('list', GuestApiView.as_view(), name='list'),
    path('create', GuestApiView.as_view(), name='create'),
    path('update', GuestApiView.as_view(), name='update'),
    path('delete/<int:pk>', GuestApiView.as_view(), name='delete'),
]


services_patterns: list[URLPattern] = [
    path('list', HotelServiceApiView.as_view(), name='list')
]

urlpatterns: list[URLPattern] = [
    path('some_url_example', hello_world),
    path('guests/', include((guests_patterns, 'guests'))),
    path('services/', include((services_patterns, 'services'))),
]
