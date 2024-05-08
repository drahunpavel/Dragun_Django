from django.shortcuts import render
from .models import Hotel, Person


# hotels = [
#     {"name": "Hilton Amsterdam Airport Schiphol",
#         "address": "Schiphol Boulevard 701, 1118 BN Schiphol, Нидерланды", "stars": 3},
#     {"name": "Burj Al Arab Jumeirah",
#         "address": "Jumeirah St - Umm Suqeim 3 - Дубай - ОАЭ", "stars": 5},
#     {"name": "Ritz Paris", "address": "15 Place Vendôme, 75001 Париж, Франция", "stars": 5},
#     {"name": "Hotel Plaza Athenee",
#         "address": "25 Avenue Montaigne, 75008 Париж, Франция", "stars": 4},
#     {"name": "Four Seasons Hotel George V",
#         "address": "31 Avenue George V, 75008 Париж, Франция", "stars": 1},
#     {"name": "The Ritz London",
#         "address": "150 Piccadilly, St. James's, Лондон W1J 9BR, Великобритания", "stars": 5},
#     {"name": "Waldorf Astoria Beverly Hills",
#         "address": "9850 Wilshire Blvd, Беверли-Хиллз, CA 90210, США", "stars": 2},
#     {"name": "Mandarin Oriental, Tokyo",
#         "address": "2 Chome-1-1 Nihonbashimuromachi, Chuo City, Токио 103-8328, Япония", "stars": 5},
#     {"name": "The Peninsula Shanghai",
#         "address": "32 Zhongshan E Rd, Wai Tan, Huangpu Qu, Shanghai Shi, Китай, 200002", "stars": 5},
#     {"name": "The Langham, Chicago",
#         "address": "330 N Wabash Ave, Чикаго, IL 60611, США", "stars": 5}
# ]


# users = [
#     {"name": "Alice", "age": 30},
#     {"name": "Bob", "age": 25},
#     {"name": "Charlie", "age": 35},
#     {"name": "David", "age": 28},
#     {"name": "Eve", "age": 40},
#     {"name": "Frank", "age": 22},
#     {"name": "Grace", "age": 32},
#     {"name": "Hannah", "age": 27},
#     {"name": "Ian", "age": 38},
#     {"name": "Jack", "age": 33}
# ]

comments = [
    {"text": "Great hotel! Will definitely come back here again.", "author": "Anna"},
    {"text": "Wonderful place to stay. Highly recommend to everyone!", "author": "Max"},
    {"text": "Excellent service, very attentive and responsive staff.", "author": "Olga"},
    {"text": "Incredible view from the room window. It was an unforgettable vacation!", "author": "Alex"},
    {"text": "Very beautiful and cozy hotel. Only positive impressions.", "author": "Maria"}
]


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


def home_template_view(request):
    return render(request=request, template_name='home.html')


def hotels_template_view(request):
    hotels = Hotel.objects.all()
    return render(request=request, template_name='hotels.html', context={'hotels': hotels})


def hotel_template_view(request, hotel_name: str):
    hotel = Hotel.objects.filter(name=hotel_name)

    if hotel:
        return render(request=request, template_name='hotel.html', context={'hotel': hotel[0], 'comments': comments})
    else:
        return render(request=request, template_name='404.html')


def users_template_view(request):
    users = Person.objects.all()
    return render(request=request, template_name='users.html', context={'users': users})


def error_404_template_view(request, exception):
    context = {}
    return render(request, '404.html', context)
