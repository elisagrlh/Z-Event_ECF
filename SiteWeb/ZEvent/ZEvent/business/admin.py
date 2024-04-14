from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


from .models import UserData
from .models import Question
from .models import Employee

#class CustomUserAdmin(UserAdmin):
 #   pass

class UserDataAdmin(admin.ModelAdmin):
    list_display = ('user', 'age', )  # Adjust fields as needed.


class UserDataInline(admin.StackedInline):
    model = UserData
    can_delete = False 
    verbose_name_plural = "employee"

class UserAdmin(BaseUserAdmin):
    inlines = [UserDataInline]

class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = "employee"


# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline]




admin.site.register(Question)
#admin.site.register(UserData, CustomUserAdmin)
#admin.site.register(UserData, UserDataAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Register your models here.
