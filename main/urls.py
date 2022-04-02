from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<str:slug>/', category_detail, name ='category'),
    path('apt-detail/<int:pk>/', apt_detail, name='detail'),
    path('add_inf/', add_information, name='add_inf'),
    path('update-info/<int:pk>/', update_info, name='update-info'),
    path('delete-info/<int:pk>', delete_info, name='delete-info'),
]