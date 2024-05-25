from multiprocessing.managers import BaseManager
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view

from .renderers import CustomRenderer
from .serializers import GuestSerializer, HotelServiceSerializer
from booking_service.models import Guest, HotelService
    

class GuestApiView(APIView):
    renderer_classes: list[type[CustomRenderer]] = [CustomRenderer]

    def get_object(self, id: int) -> Guest:
        try:
            return Guest.objects.get(id=id)
        except Guest.DoesNotExist:
            raise Http404

    def get(self, request) -> Response:
        guests: BaseManager[Guest] = Guest.objects.all()
        serializer = GuestSerializer()
        serialized_data = [serializer.serialize_guest(guest) for guest in guests]
        return Response(serialized_data, status=status.HTTP_200_OK)


    def put(self, request) -> Response:
        guest_id: int = request.data.get('id')

        if not guest_id:
            return Response({"error": "no guest_id"},status=status.HTTP_404_NOT_FOUND)

        guest: Guest = self.get_object(guest_id)
        # guest - instance, сериализатор принимает instance и понимает, что это update 
        serializer = GuestSerializer(guest, data=request.data)
        if serializer.is_valid():
            serializer.save() # вызывает метод create() в сериализаторе
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request) -> Response:
        guest = GuestSerializer(data=request.data)

        if guest.is_valid():
            guest.save() # вызывает метод update() в сериализаторе
            return Response(guest.data, status=status.HTTP_201_CREATED)
        return Response(guest.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk) -> Response:
        guest: Guest = self.get_object(pk)
        serializer = GuestSerializer()
        serializer.delete(guest)
        return Response({"message": "Guest deleted"})

class HotelServiceApiView(APIView):
    def get(self, request) -> Response:
        services: BaseManager[HotelService] = HotelService.objects.all()
        serializer = HotelServiceSerializer(services, many=True)
        return Response(serializer.data)



@api_view(['GET'])
def hello_world(requst) -> Response:
    return Response({"message": "Hello, world!"})