from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import FacebookRoom
from .serializers import RoomIsBookedSerializer, RoomIsNotBookedSerializer


# Create your views here.
class FacebookRoomView(APIView):
    def get(self, request, room_number):
        try:
            room = FacebookRoom.objects.get(room_number=room_number)
            #
            if room.is_booked:
                serializer = RoomIsBookedSerializer(room)

                msg = "Xona allaqachon boshqa bir mijoz tomonidan band qilingan!"
                data = {
                    "message": msg,
                    "available_from": serializer.data.values()
                }
                return Response(data, status=status.HTTP_409_CONFLICT)
            else:
                serializer = RoomIsNotBookedSerializer(room)

                msg = "Xona band qilinmagan!"
                data = {
                    "message": msg,
                    "available_from": serializer.data.values()
                }
                return Response(data, status=status.HTTP_201_CREATED)

        except FacebookRoom.DoesNotExist:
            return Response({"message": "Xona topilmadi yoki mavjud emas xona raqami kiritildi!"}, status=status.HTTP_404_NOT_FOUND)


def hello_world(request):
    return HttpResponse("Hello, World!")
