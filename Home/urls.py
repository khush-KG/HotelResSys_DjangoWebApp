from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('login/', login_page, name="login"),
    path('register/', register_page, name="register"),
    path('hotel-detail/<uid>/', hotel_detail, name="hotel_detail"),
    path('check_booking/' , check_booking),
    path("checkUsers/", checkUsers, name="checkUsers")
]
