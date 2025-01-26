from django.contrib import admin
from .models import UserMessages,Room,CustomUser
# Register your models here.

admin.site.register(UserMessages)
admin.site.register(Room)

admin.site.register(CustomUser)