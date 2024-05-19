from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Prefetch
from .models import Booking, Guest, Hotel, HotelComment, Room
from django.db import transaction
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


def book_room_view(request, hotel_name: str, user_id: int, room_number: int):
    context = {
        'hotel_name': hotel_name,
        'user_id': user_id,
        'room_number': room_number,
        'info': ''
    }

    try:
        hotel = Hotel.objects.get(name=hotel_name)
        print('--hotel', hotel)
    except Hotel.DoesNotExist:
        context['hotel_name'] = 'Hotel is not found'
        return render(request, 'book.html', context)

    try:
        guest = Guest.objects.get(id=user_id)
        print('--guest', guest)
    except Guest.DoesNotExist:
        context['user_id'] = 'User is not found'
        return render(request, 'book.html', context)

    try:
        room = Room.objects.get(hotel=hotel, number=room_number)
        print('--room', room)
    except Room.DoesNotExist:
        context['room_number'] = 'Room is not found'
        return render(request, 'book.html', context)

    # транзакционное изменение
    with transaction.atomic():
        # проверка, есть ли актуальная бронь на данный номер в данном отеле
        # exists - проверяет наличие объектов в QuerySet, возвращает True\False
        if Booking.objects.filter(hotel=hotel, room=room).exists():
            context['info'] = f'hotel room: {str(room_number)} booked'
            return render(request, 'book.html', context)

        Booking.objects.create(
            guest=guest,
            hotel=hotel,
            room=room,
            details="Booking details from book_room_view",
            check_in_date=timezone.now(),
            check_out_date=timezone.now() + timedelta(days=7),  # +7 дней
        )
        room.is_booked = True
        room.save()
        # Room.objects.filter(number=room.number).update(is_booked=True)

    return render(request, 'book.html', context)


def error_404_view(request, exception):
    context = {}
    return render(request, '404.html', context)
