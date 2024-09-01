from django.urls import path

from . import views

urlpatterns=[
    path('',views.getData,name='getData'),
    path('getResult',views.getResult,name='getResult')
]