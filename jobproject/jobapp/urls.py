from django.urls import path
from jobapp import views
urlpatterns=[
    path('home/',views.home),
    path('hydjob/',views.Hydjob),
    path('chenjob/',views.Chenjob),
    path('bangjob/',views.Bangjob)
]