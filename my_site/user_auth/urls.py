from django.urls import path
from . import views



app_name = 'user_auth'

urlpatterns = [
    path('register/', views.user_register, name='user_register'),
    path('login/', views.user_login, name='user_login'),
]

