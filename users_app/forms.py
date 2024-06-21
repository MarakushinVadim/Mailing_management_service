from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.forms import ModelForm

from mailing_interface_app.forms import StyleFormMixin
from users_app.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserPasswordResetForm(StyleFormMixin, PasswordResetForm):
    class Meta:
        model = User
        fields = ('email',)


class UserModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = User
        fields = ('is_active',)
