from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import admin as auth_admin
from forms import UserChangeForm, UserCreationForm

@admin.register(CustomUser)
class UserAdmin(auth_admin.UserAdmin):
    form = UserCreationForm
    add_form = UserChangeForm
    model = CustomUser
    fieldsets = ('teste')


admin.site.register(CustomUser, UserAdmin)
# Register your models here.
