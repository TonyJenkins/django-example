# Generated by Django 5.0.7 on 2024-07-22 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_list', '0003_alter_room_building'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='building',
            field=models.CharField(choices=[('Turing', 'Turing'), ('Lovelace', 'Lovelace')], max_length=12),
        ),
    ]