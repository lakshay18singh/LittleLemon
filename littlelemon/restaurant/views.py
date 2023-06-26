from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
# Create your views here.

def index(request):
          return render(request, 'index.html', {})
@permission_classes([IsAuthenticated])
class MenuItemView(ListCreateAPIView):
        queryset = Menu.objects.all()
        serializer_class = MenuSerializer
        #permission_classes = [IsAuthenticated]

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
        queryset = Menu.objects.all()
        serializer_class = MenuSerializer
        permission_classes = [IsAuthenticated]

class BookingViewSet(ModelViewSet):
        queryset = Booking.objects.all()
        serializer_class = BookingSerializer
        permission_classes = [IsAuthenticated]
