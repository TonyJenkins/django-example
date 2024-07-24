from django.shortcuts import render

from .models import Tutor


def all_staff_list(request):

    staff = Tutor.objects.all()

    context = {
        'staff': staff,
    }

    return render(request, 'staff_list/all_staff_list.html', context,)
