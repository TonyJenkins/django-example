from django.contrib import admin

from .models import Room, Faculty, Tutor

admin.site.register(Room)
admin.site.register(Faculty)


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):

    list_display = [
            'surname',
            'forenames',
            'email',
            'room',
            'faculty',
        ]

    prepopulated_fields = {
        'slug': ('surname', 'forenames'),
    }

    list_filter = [
        'room',
        'faculty',
    ]

    ordering = [
        'surname',
        'forenames',
    ]

    show_facets = admin.ShowFacets.ALWAYS
