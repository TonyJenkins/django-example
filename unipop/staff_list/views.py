from django.shortcuts import render

from .models import Tutor


def all_staff_list(request):

    staff = Tutor.objects.all()

    context = {
        'staff': staff,
    }

    return render(request, 'staff_list/all_staff_list.html', context,)


def staff_detail(request, tutor_id):

    staff_details = Tutor.objects.get(pk=tutor_id)

    context = {
        'staff_details': staff_details,
    }

    return render(request, 'staff_list/staff_detail.html', context)


def staff_detail_from_slug(request, slug):

    staff_details = Tutor.objects.get(slug=slug)

    context = {
        'staff_details': staff_details,
    }

    return render(request, 'staff_list/staff_detail.html', context)


def staff_list_by_faculty(request):

    staff = (Tutor.objects
             .all()
             .order_by('faculty__name', 'surname', 'forenames'))

    context = {
        'staff': staff,
    }

    return render(request, 'staff_list/all_staff_list_by_faculty.html', context,)
