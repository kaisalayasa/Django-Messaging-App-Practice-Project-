# Generated by Django 5.1.4 on 2025-01-08 20:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_add_predefined_rooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermessages',
            name='room',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='Base.room'),
        ),
    ]
