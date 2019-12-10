from django.urls import path

from . import views


 
urlpatterns = [path("",views.front, name='front'),
                path('signUp/', views.signUp, name='signUp'),
                path('login/',views.login, name='login'),
                path('logout/',views.logout,name='logout'),
                path('complaints/',views.list, name='complaints'),
                path('Electricity/',views.Electricity, name='Electricity'),
                path('Plumber/',views.Plumber, name='plumber'),
                path('Air_conditioner/',views.Air_conditioner, name='Air_conditioner'),
                path('Room_cleaning/',views.Room_cleaning, name='Room_cleaning'),
                path('Carpanter/', views.Carpanter, name='Carpanter'),
]
