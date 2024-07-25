from django.urls import path
from . import views

app_name = 'staff_list'

urlpatterns = [
    path('',
         views.all_staff_list,
         name='all_staff_list'
         ),
    path('<int:tutor_id>/',
         views.staff_detail,
         name='staff_detail'
         ),
    path('<slug:slug>/',
         views.staff_detail_from_slug,
         name='staff_detail_from_slug'
         ),
]
