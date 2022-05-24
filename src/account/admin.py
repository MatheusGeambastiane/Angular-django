from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import admin as auth_admin
# from .forms import UserChangeForm, UserCreationForm

@admin.register(CustomUser)
class UserAdmin(auth_admin.UserAdmin):
    # form = UserCreationForm
    # add_form = UserChangeForm
    model = CustomUser
    # readonly_fields = ('password',)
    list_display = ('username', 'manager_status', 'costumer_status')
    search_fields = ('username',)
    fieldsets = (
        (None, {"fields": ("username", "password", "costumer_status", "manager_status")}),
        
        (
            ("Permissions"),
            {
                "fields": (
                    
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "teste"),
            },
        ),
    )