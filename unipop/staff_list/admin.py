from django.contrib import admin

from .models import Room, Faculty, Tutor

admin.site.register(Room)
admin.site.register(Faculty)


@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):

    list_display = [
            'name',
            'room',
            'faculty',
        ]

    list_filter = [
        'room',
        'faculty',
    ]

    ordering = [
        'name',
    ]

    show_facets = admin.ShowFacets.ALWAYS
