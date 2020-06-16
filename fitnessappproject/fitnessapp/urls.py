from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('getweight/', views.getweight, name='weight'),
    path('getworkout/', views.getworkout, name='workout'),
    path('getmeals/', views.getmeals, name='meals'),
    path('newWorkout', views.newWorkout, name='newworkout'),
    path('newWeight', views.newWeight, name='newweight'),
    path('newMeal', views.newMeal, name='newmeal'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('loginmessage', views.loginmessage, name='loginmessage'),
    path('logoutmessage', views.logoutmessage, name='logoutmessage'),
]