from django.contrib.auth import forms

from .models import CustomUser


# class UserChangeForm(forms.UserChangeForm):
#     class Meta:
#         model = CustomUser
#         # fields = ('username', 'is_active', 'teste')


# class UserCreationForm(forms.UserCreationForm):
#     class Meta(forms.UserCreationForm.Meta):
#         model = CustomUser
#         # fields = ('username', 'is_active', 'teste')
    