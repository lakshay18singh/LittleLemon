from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from . import views
from rest_framework.authtoken.views import obtain_auth_token



urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menuView),
    path('booking/', views.bookingView),
    path('api-token-auth/', obtain_auth_token),
    path('testing/', views.managerBookingView),
    path('manager/', views.managerGetView),
    path('manager/post/', views.managerPostView),
    path('manager/delete/', views.managerDeleteView),
    path('manager/booking/', views.managerBookingView),
    path('register/', views.registerView),
    path('login/', views.loginView),
    path('logout/', views.logoutView)
]