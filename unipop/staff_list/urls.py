from django.urls import path
from . import views

app_name = 'staff_list'

urlpatterns = [
    path('',
         views.all_staff_list,
         name='all_staff_list'
         ),

    path('faculty/',
         views.staff_list_by_faculty,
         name='staff_list_by_faculty'
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
