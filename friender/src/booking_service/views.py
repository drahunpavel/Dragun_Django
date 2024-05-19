from django.shortcuts import render
from django.db.models import Prefetch
from .models import Booking, Guest, Hotel, HotelComment

# def get_hotel_by_name(hotel_name):
#     hotel = Hotel.objects.filter(name__in=[hotel_name])
#     if hotel:
#         return hotel
#     else:
#         return None
# for hotel in hotels:
#     if hotel['name'] == hotel_name:
#         return hotel
# return None


# def home_view(request):
#     return HttpResponse('home')


def home_view(request):
    return render(request=request, template_name='home.html')


def hotels_view(request):
    # hotels = Hotel.objects.all()
    hotels = Hotel.objects.prefetch_related('comments').all()
    # hotels = Hotel.objects.prefetch_related(Prefetch('comments', queryset=HotelComment.objects.all())).all()

    # hotel_comments_dict = {}

    # for hotel in hotels:
    #     hotel_comments_dict[hotel.id] = list(hotel.comments.all())

    hotels_list = []

    # for hotel in hotels:
    #     hotels_list.append({'hotel': hotel, 'comments': hotel_comments_dict.get(hotel.id, [])})

    for hotel in hotels:
        # comments = HotelComment.objects.filter(hotel__name=hotel.name)
        # hotels_list.append({'hotel': hotel, 'comments': comments})
        hotels_list.append({'hotel': hotel, 'comments': hotel.comments.all()})

    context = {'hotels': hotels_list}

    return render(request=request, template_name='hotels.html', context=context)


def hotel_view(request, hotel_name: str):
    hotel = Hotel.objects.filter(name=hotel_name)
    comments = HotelComment.objects.filter(hotel__name=hotel_name)

    comment_list = []

    for comment in comments:
        guest_name = comment.guest.first_name
        comment_text = comment.text
        comment_list.append({'name': guest_name, 'text': comment_text})

    if hotel:
        return render(request=request, template_name='hotel.html', context={'hotel': hotel[0], 'comments': comment_list})
    else:
        return render(request=request, template_name='404.html')


def users_view(request):
    guests = Guest.objects.all()

    guests_list = []

    for guest in guests:
        bookings = Booking.objects.filter(
            guest_id=guest.id).prefetch_related('hotel_services')
        services_list = []
        for booking in bookings:
            for service in booking.hotel_services.all():
                services_list.append(service.name)
        guests_list.append({'guest': guest, 'services': services_list})

    context = {
        'guests': guests_list,
    }

    return render(request=request, template_name='users.html', context=context)


def error_404_view(request, exception):
    context = {}
    return render(request, '404.html', context)
