from django.urls import path
from newsapp import views
urlpatterns=[
    path('index/',views.index),
    path('moviesinfo/',views.moviesinfo),
    path('sportsinfo/',views.sportsinfo),
    path('politicsinfo',views.politicsinfo)
]
