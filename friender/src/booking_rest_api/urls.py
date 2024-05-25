from django.urls import URLPattern, path

from .views import GuestApiView, hello_world



urlpatterns: list[URLPattern] = [
    path('some_url_example', hello_world),
    path('guests/list', GuestApiView.as_view(), name='guest_list'),
    path('guests/create', GuestApiView.as_view(), name='guest_create'),
    path('guests/update', GuestApiView.as_view(), name='guest_update'),
    path('guests/delete/<int:pk>', GuestApiView.as_view(), name='guest_delete'),
]
