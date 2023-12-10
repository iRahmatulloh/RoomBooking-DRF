from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, filters
from django.utils import timezone
from django_filters.rest_framework import DjangoFilterBackend

from .models import FacebookRoom, GoogleRoom, AmazonRoom, HuluRoom, NetflixRoom
from .serializers import RoomIsBookedSerializer, RoomIsNotBookedSerializer, RoomListSerializer


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
                print(serializer.data)
                msg = "Xona band qilinmagan!"
                data = {
                    "message": msg,
                    "room": serializer.data
                }
                return Response(data, status=status.HTTP_201_CREATED)

        except FacebookRoom.DoesNotExist:
            return Response({"message": "Xona topilmadi yoki mavjud emas xona raqami kiritildi!"}, status=status.HTTP_404_NOT_FOUND)


class GoogleRoomView(APIView):
    def get(self, request, room_number):
        try:
            room = GoogleRoom.objects.get(room_number=room_number)
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
                print(serializer.data)
                msg = "Xona band qilinmagan!"
                data = {
                    "message": msg,
                    "room": serializer.data
                }
                return Response(data, status=status.HTTP_201_CREATED)

        except GoogleRoom.DoesNotExist:
            return Response({"message": "Xona topilmadi yoki mavjud emas xona raqami kiritildi!"}, status=status.HTTP_404_NOT_FOUND)


class AmazonRoomView(APIView):
    def get(self, request, room_number):
        try:
            room = AmazonRoom.objects.get(room_number=room_number)
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
                print(serializer.data)
                msg = "Xona band qilinmagan!"
                data = {
                    "message": msg,
                    "room": serializer.data
                }
                return Response(data, status=status.HTTP_201_CREATED)

        except AmazonRoom.DoesNotExist:
            return Response({"message": "Xona topilmadi yoki mavjud emas xona raqami kiritildi!"}, status=status.HTTP_404_NOT_FOUND)


class NetflixRoomView(APIView):
    def get(self, request, room_number):
        try:
            room = NetflixRoom.objects.get(room_number=room_number)
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
                print(serializer.data)
                msg = "Xona band qilinmagan!"
                data = {
                    "message": msg,
                    "room": serializer.data
                }
                return Response(data, status=status.HTTP_201_CREATED)

        except NetflixRoom.DoesNotExist:
            return Response({"message": "Xona topilmadi yoki mavjud emas xona raqami kiritildi!"}, status=status.HTTP_404_NOT_FOUND)


class HuluRoomView(APIView):
    def get(self, request, room_number):
        try:
            room = HuluRoom.objects.get(room_number=room_number)
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
                print(serializer.data)
                msg = "Xona band qilinmagan!"
                data = {
                    "message": msg,
                    "room": serializer.data
                }
                return Response(data, status=status.HTTP_201_CREATED)

        except HuluRoom.DoesNotExist:
            return Response({"message": "Xona topilmadi yoki mavjud emas xona raqami kiritildi!"}, status=status.HTTP_404_NOT_FOUND)


class AllRoomView(APIView):
    def get(self, request):
        facebook_rooms = FacebookRoom.objects.filter(is_booked=False)
        google_rooms = GoogleRoom.objects.filter(is_booked=False)
        amazon_rooms = AmazonRoom.objects.filter(is_booked=False)
        netflix_rooms = NetflixRoom.objects.filter(is_booked=False)
        hulu_rooms = HuluRoom.objects.filter(is_booked=False)

        facebook_serializer = RoomListSerializer(facebook_rooms, many=True)
        google_serializer = RoomListSerializer(google_rooms, many=True)
        amazon_serializer = RoomListSerializer(amazon_rooms, many=True)
        netflix_serializer = RoomListSerializer(netflix_rooms, many=True)
        hulu_serializer = RoomListSerializer(hulu_rooms, many=True)

        data = {
            "facebook_rooms": facebook_serializer.data,
            "google_rooms": google_serializer.data,
            "amazon_rooms": amazon_serializer.data,
            "netflix_rooms": netflix_serializer.data,
            "hulu_rooms": hulu_serializer.data,
            'today': timezone.now()
        }

        return Response(data)


class EndTimeFilterView(generics.ListAPIView):
    queryset = FacebookRoom.objects.all()
    serializer_class = RoomIsBookedSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['$end_time']


def hello_world(request):
    return HttpResponse("Hello, World!")

