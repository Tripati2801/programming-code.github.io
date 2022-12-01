from django.urls import path
from movieapp import views
urlpatterns=[
    path('index/',views.index),
    path('listmovie/',views.listmovie),
    path('addmovie/',views.addmovie)
]