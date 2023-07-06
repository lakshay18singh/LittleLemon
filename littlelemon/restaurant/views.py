from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .forms import MenuForm, BookingForm, altBooking
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.generic.edit import FormView
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from math import ceil

# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def bookingView(request):
        form = BookingForm(user = request.user)
        description = ''
        if request.method == "POST":
                form = BookingForm(request.POST, user = request.user)
                if form.is_valid():
                        description = 'Booking Successfully done on ' + str(form.cleaned_data['BookingDate'])
                        form.save()
                else:
                        description = "Incorrect Form Data Entered"
                        
                
        context = {'form': form, 'description': description}
        return render(request, 'booking.html', context)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def menuView(request):
        menuobj = Menu.objects.all()
        #sermenu = MenuSerializer(menuobj, many=True)
        perpage = request.GET.get('perpage', default=4)
        page = request.GET.get('page', default = 1)
        paginator = Paginator(menuobj, per_page=perpage)
        try:
                objpg = paginator.page(page)
        except EmptyPage:
                objpg = []

        numPage = ceil(len(menuobj) / int(perpage))
        menu_dict = {}
        for item in objpg:
             menu_dict[item.Title] = {'Description': item.Description,
                                      'Price': item.Price}
        #print('Send')
        return render(request, 'menu.html', {'menu': menu_dict, 'numPage': list(range(1, numPage+ 1))})

@api_view(['GET']) 
@permission_classes([IsAuthenticated])     
def managerBookingView(request):
        if request.user.groups.filter(name='Manager').exists():
                bookingobj = Booking.objects.all()
                perpage = request.GET.get('perpage', default=3)
                page = request.GET.get('page', default = 1)
                paginator = Paginator(bookingobj, per_page=perpage)
                numPage = ceil(len(bookingobj) / int(perpage))
                try:
                        objpg = paginator.page(page)
                except EmptyPage:
                        objpg = []


                Booking_dict = {}

                
                
                for item in objpg:
                        Booking_dict[item.id] = {'BookingDate': item.BookingDate,
                                                 'Name': item.Name,
                                                 'No_of_guests': item.No_of_guests }
                
                return render(request, 'managerBooking.html', {'menu': Booking_dict, 'numPage': list(range(1, numPage+ 1))})
        else:
                return HttpResponse("Not Authorized", status = 400)



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def managerGetView(request):
        if request.user.groups.filter(name='Manager').exists():
                menuobj = Menu.objects.all()
                #sermenu = MenuSerializer(menuobj, many=True)
                perpage = request.GET.get('perpage', default=3)
                page = request.GET.get('page', default = 1)
                paginator = Paginator(menuobj, per_page=perpage)
                numPage = ceil(len(menuobj) / int(perpage))
                try:
                        objpg = paginator.page(page)
                except EmptyPage:
                        objpg = []


                menu_dict = {}
                for item in objpg:
                        menu_dict[item.Title] = {'Description': item.Description,
                                                 'Price': item.Price,
                                                 'Id': item.Id }
                #print('Send')
                return render(request, 'managerGet.html', {'menu': menu_dict, 'numPage': list(range(1, numPage+ 1))})
        else:
                return HttpResponse("Not Authorized", status = 400)

@permission_classes([IsAuthenticated])
def managerPostView(request):
        if request.user.groups.filter(name='Manager').exists():
                
                description=""
                if request.method == "POST":
                        form = MenuForm(request.POST)
                        if form.is_valid():
                                messages.success(request, 'Item added to menu Successfully')
                                
                                form.save()
                        else:
                                description = "Incorrect Form Data Entered"
                                #print('Nhi Chala')
                form = MenuForm()
                context = {'form': form, 'description': description}
                return render(request, 'managerPost.html', context)

        else:
                return HttpResponse("Not Authorized", status = 400)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def managerDeleteView(request):
        if request.user.groups.filter(name='Manager').exists():
                
                
                if request.method == "POST":
                        menuId = int(request.POST.get('menuId'))
                        inst = Menu.objects.filter(Id = menuId)
                        if not inst:
                                messages.success(request, f'Menu Item with Id = {menuId} doesn\'t exist')
                        else:
                                messages.error(request, inst[0].Title + ' deleted from menu Successfully')
                                inst.delete()
                        
                return render(request, 'managerDelete.html', {})
        return HttpResponse("Not Authorized", status = 400)
        

def registerView(request):
        if request.method == 'POST':
                form = UserCreationForm(request.POST)
                if form.is_valid():
                        user = form.save()
                        login(request, user)
                        return redirect('../')
        form = UserCreationForm()
        context = {'request_form': form}
        return render(request, 'register.html', context)
  

def loginView(request):
        if request.method == 'POST':
                form = AuthenticationForm(request, data = request.POST)
                if form.is_valid():
                        username = form.cleaned_data.get('username')
                        password = form.cleaned_data.get('password')
                        user = authenticate(username = username, password = password)
                        if user is not None:
                              login(request, user)
                              if request.user.groups.filter(name='Manager').exists():
                                      return redirect('../manager/')
                              else:
                                return redirect('../')  
                        else:
                                return HttpResponse('User does not exist')
                else:
                        return HttpResponse('Incorrect Login Info')
        form = AuthenticationForm()
        context = {'login_form': form}
        return render(request, 'login.html', context)

def logoutView(request):
        logout(request)

        return redirect('../')


def index(request):
          if request.user.is_authenticated:      
                return render(request, 'index.html', {})
          else:
                 return redirect('login/')



