from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user-list', views.index, name='user-list'),
]