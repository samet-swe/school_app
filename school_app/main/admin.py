from django.contrib import admin
from .models import User, Room

class UserAdmin(admin.ModelAdmin):
    list_display = ("last_name", "first_name", "username", "role", "display_room")
    search_fields = ("first_name", "last_name", "username", "room__name")
    list_filter = ("role", )
    
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "display_members")
    search_fields = ("name", )
    
admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)
