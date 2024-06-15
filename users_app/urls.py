from django.urls import path

from users_app.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, UserDetailView

urlpatterns = [
    path('users_app/user_list/', UserListView.as_view(), name='user_list'),
    path('users_app/user_create/', UserCreateView.as_view(), name='user_create'),
    path('users_app/user_update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('users_app/user_delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('users_app/user_detail/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]