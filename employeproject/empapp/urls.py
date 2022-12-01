from django.urls import path
from empapp import views
urlpatterns=[
    path('emp/',views.empdata)
]