from django.urls import path

from . import views

urlpatterns=[
    path('',views.getData,name='getData'),
    path('predict',views.predict,name='predict')
]