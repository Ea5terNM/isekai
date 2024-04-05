from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import Profile, CustomUser


class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("email",)

class UserProfilesForm(forms.ModelForm):  # แก้จาก UserProfilesform เป็น UserProfilesForm
    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name")

class ExtendedProfilesForm(forms.ModelForm):  # แก้จาก extendedProfilesForm เป็น ExtendedProfilesForm
    prefix = "extended"
    class Meta:
        model = Profile
        fields = ("address", "phone")
        labels = {
            "address": "ที่อยู่",
            "phone": "เบอร์โทรศัพท์",
        }

