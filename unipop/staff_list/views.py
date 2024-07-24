from django.shortcuts import render


def all_staff_list(request):
    return render(request, 'staff_list/all_staff_list.html')
