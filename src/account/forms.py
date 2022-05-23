from django.contrib.auth import forms

from .models import CustomUser


class UserChangeForm(forms.UserChangeForm):
    class Meta(forms.UserChangeForm.Meta):
        model = CustomUser


class UserCreationForm(forms.UserCreationForm):
    class Meta(forms.UserCreationForm.Meta):
        model = CustomUser