from django import forms
from django.forms import ModelForm, PasswordInput, TextInput


class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        widgets = {
            "username": TextInput(attrs={"type": "text", "name": "name", "id": "name"}),
            "password": PasswordInput(
                attrs={"type": "password", "name": "pass", "id": "pass"}
            ),
        }
