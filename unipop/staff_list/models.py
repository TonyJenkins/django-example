from django.db import models


class Room(models.Model):
    number = models.CharField(max_length=8)
    building = models.CharField(max_length=16)


class Faculty(models.Model):
    name = models.CharField(max_length=64)
    dean = models.CharField(max_length=64, null=True)

    class Meta:
        verbose_name_plural='Faculties'


class Tutor(models.Model):
    name = models.CharField(max_length=64)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
