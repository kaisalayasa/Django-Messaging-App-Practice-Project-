# Generated by Django 5.1.4 on 2025-01-07 22:13

from django.db import migrations


class Migration(migrations.Migration):
    def create_predefined_rooms(apps, schema_editor):
        Room = apps.get_model('Base', 'Room')
        predefined_rooms = ['wallmart', 'other location', 'general chat']
        for room_name in predefined_rooms:
            Room.objects.get_or_create(name=room_name)

    dependencies = [
        ('Base', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_predefined_rooms),
    ]
