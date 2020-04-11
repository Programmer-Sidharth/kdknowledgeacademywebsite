from django.urls import path
from .views import *
from django.conf.urls.static import static
from KD import settings
urlpatterns = [
    path('', index),
    path('rollno/<str:id>/', student),
    path('register/', register),
    path('login/', login),
    path('login/myaccount/', profile),
    path('cources/', cources),
    path('class<str:standard>/students', students_on_class),
    path('register/user/', registered),
    path('friends/', find_friends),
    path('friends/user/', friendifound),
]