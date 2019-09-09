from django.urls import path,re_path
from . import views
from rythubazarapp.views import *
from django.conf import settings

urlpatterns = [
    path('', Homepage.as_view(), name="homepage"),
    path('home/', Homepage.as_view(), name="homepage"),
    path('farmer_login/', AddINventory.as_view(), name="add inventory items"),
    path('buyer_login/', DisplayInventory.as_view(), name="all items to buy"),
    path('home/farmer_login/', AddINventory.as_view(), name="add inventory items1"),
    path('home/buyer_login/', DisplayInventory.as_view(), name="all items to buy1"),
    path('login/', LoginController.as_view(), name='login'),
    path('signup/', SignupController.as_view(), name='signup'),
    path('logout/', logout_user, name='logout'),
]
