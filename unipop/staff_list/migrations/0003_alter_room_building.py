# Generated by Django 5.0.7 on 2024-07-22 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_list', '0002_alter_faculty_options_alter_room_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='building',
            field=models.CharField(choices=[('TU', 'Turing'), ('LO', 'Lovelace')], max_length=2),
        ),
    ]