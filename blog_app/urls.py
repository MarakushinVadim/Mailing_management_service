from django.urls import path

from blog_app.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView
from users_app.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('blog_app/blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_app/blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_app/blog_detail/<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('blog_app/blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_app/blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
