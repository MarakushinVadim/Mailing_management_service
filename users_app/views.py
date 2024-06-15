from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView

from users_app.models import User


class UserCreateView(CreateView):
    model = User


class UserDetailView(DetailView):
    model = User


class UserUpdateView(UpdateView):
    model = User


class UserDeleteView(DeleteView):
    model = User


class UserListView(ListView):
    model = User
