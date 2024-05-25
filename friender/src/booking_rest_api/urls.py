from django.urls import URLPattern, include, path

from .views import GuestApiView, hello_world


guests_patterns: list[URLPattern] = [
    path('list', GuestApiView.as_view(), name='guest_list'),
    path('create', GuestApiView.as_view(), name='guest_create'),
    path('update', GuestApiView.as_view(), name='guest_update'),
    path('delete/<int:pk>', GuestApiView.as_view(), name='guest_delete'),
]


urlpatterns: list[URLPattern] = [
    path('some_url_example', hello_world),
    path('guests/', include((guests_patterns, 'guests'))),
]
