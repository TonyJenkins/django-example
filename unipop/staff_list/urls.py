from django.urls import path
from . import views

app_name = 'staff_list'

urlpatterns = [
    path('',
         views.all_staff_list,
         name='all_staff_list'
         ),
    ]
