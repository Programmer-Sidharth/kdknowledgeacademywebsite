from django.urls import path
from .views import *
from django.conf.urls.static import static
from KD import settings
urlpatterns = [
    path('', index),
    path('rollno/<str:id>/', student),
    path('profile/', editingProfile_home),
    path('register/', register),
    path('profile/update-details/', updateProfile),
    path('login/', login),
    path('logout/', logout),
    path('login/myaccount/', profile),
    path('cources/', cources),
    path('class<str:standard>/', standard_details),
    path('class<str:standard>/students/', students_on_class),
    path('class<str:standard>/buy/', buy_cource),
    path('register/user/', registered),
    path('search_students/', search_students),
    path('search_students/user/', friendifound),
]