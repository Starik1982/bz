from django.contrib import admin
from .models import *

class PersonalRoomAdmin(admin.TabularInline):
    model = PersonalRoom
    extra = 0

class PersonalRoomAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in PersonalRoom._meta.fields]

    class Meta:
        model = PersonalRoom

admin.site.register(PersonalRoom, PersonalRoomAdmin)
