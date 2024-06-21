from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users_app.apps import UsersConfig
from users_app.views import UserCreateView, email_verification, UserPasswordResetView, UserListView, UserDetailView, \
    UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', UserCreateView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('password_reset_form', UserPasswordResetView.as_view(), name='password_reset_form'),
    path('user_list', UserListView.as_view(), name='user_list'),
    path('user_detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]
