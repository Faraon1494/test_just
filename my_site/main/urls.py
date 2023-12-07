from django.urls import path
from . import views



app_name = 'name'

urlpatterns = [
    path('', views.index, name='index'),
    path('cheap/', views.cheap, name='cheap'),
    path('item/<int:item_id>/', views.detail, name = 'detail'),
   path('add/', views.add_product, name='add')
]


