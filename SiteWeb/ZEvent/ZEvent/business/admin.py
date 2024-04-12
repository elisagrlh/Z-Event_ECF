from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import UserData
from .models import Question

#class CustomUserAdmin(UserAdmin):
 #   pass

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', )  # Adjust fields as needed.

admin.site.register(Question)
#admin.site.register(UserData, CustomUserAdmin)
admin.site.register(UserData, UserDataAdmin)

# Register your models here.
