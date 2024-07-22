from django.db import models


class Room(models.Model):

    class Building(models.TextChoices):
        TURING = 'Turing'
        LOVELACE = 'Lovelace'

    number = models.CharField(max_length=8)
    building = models.CharField(
        max_length=12,
        choices=Building,
    )

    class Meta:
        ordering = [
            'building',
            'number',
        ]
        unique_together = [
            'number',
            'building',
        ]

    def __str__(self):
        return f'{self.number}, {self.building}'


class Faculty(models.Model):
    name = models.CharField(max_length=64)
    dean = models.CharField(max_length=64, null=True)

    class Meta:
        ordering = [
            'name',
        ]
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return self.name


class Tutor(models.Model):
    name = models.CharField(max_length=64)
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, related_name='members')
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True, related_name='occupants')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            'name',
        ]

    def __str__(self):
        return self.name
