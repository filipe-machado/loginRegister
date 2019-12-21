from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('user-list', views.listUser, name='user-list'),
    path('new-user', views.newUser, name='new-user'),
    path('delete-user/<int:id>', views.deleteUser, name='delete-user'),
    path('edit-user/<int:id>', views.editUser, name='edit-user'),
]