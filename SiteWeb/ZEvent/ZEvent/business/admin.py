from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from .models import UserData

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', )  # Adjust fields as needed.


class UserDataInline(admin.StackedInline):
    model = UserData
    can_delete = False 
    verbose_name_plural = "employee"

class UserAdmin(BaseUserAdmin):
    inlines = [UserDataInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
