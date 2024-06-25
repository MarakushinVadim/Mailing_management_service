import secrets

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
    ListView,
)

from Mailing_management_service.settings import EMAIL_HOST_USER
from users_app.forms import UserRegisterForm, UserPasswordResetForm, UserModeratorForm
from users_app.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_app:login")

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f"http://{host}/users_app/email-confirm/{token}/"
        send_mail(
            subject="Подтверждение почты",
            message=f"Привет, перейди по ссылке для подтверждения почты {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users_app:login"))


class UserPasswordResetView(PasswordResetView):
    model = User
    form_class = UserPasswordResetForm
    success_url = reverse_lazy("users_app:login")

    def form_valid(self, form):
        if self.request.method == "POST":
            user_email = self.request.POST.get("email")
            user = User.objects.filter(email=user_email).first()
            base_user = BaseUserManager
            if user:
                new_password = base_user.make_random_password(user)
                user.set_password(new_password)
                user.save()
                try:
                    send_mail(
                        subject="Новый пароль",
                        message=f"Ваш новый пароль: {new_password}",
                        from_email=EMAIL_HOST_USER,
                        recipient_list=[user.email],
                    )
                except Exception:
                    print(f"Ошибка при отправке письма, {user.email}")
                return HttpResponseRedirect(reverse("users_app:login"))


class UserDetailView(DetailView):
    model = User

    def get_form_class(self):
        user = self.request.user
        if user.has_perm("users_app.can_edit_is_active"):
            return UserModeratorForm
        raise PermissionDenied


class UserListView(LoginRequiredMixin, ListView):
    model = User

    def get_queryset(self):
        user = self.request.user
        if user.has_perm("users_app.can_view_users"):
            return User.objects.all()
        raise PermissionDenied


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserModeratorForm
    success_url = reverse_lazy("users_app:user_list")
