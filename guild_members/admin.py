from django.contrib import admin
from .models import *


class GuildMembersAdmin(admin.TabularInline):
    model = GuildMembers
    extra = 0

class GuildMembersAdmin (admin.ModelAdmin):
    list_display = [field.name for field  in GuildMembers._meta.fields]

    class Meta:
        model = GuildMembers

admin.site.register(GuildMembers, GuildMembersAdmin)



