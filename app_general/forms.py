from django import forms
from users.models import UserFavoriteitem


class FavoriteitemForm(forms.ModelForm):
    class Meta:
        model = UserFavoriteitem
        fields = ["like"]
        widgets = {"like": forms.HiddenInput}


