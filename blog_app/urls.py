from django.urls import path
from django.views.decorators.cache import cache_page

from blog_app.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('blog_app/blog_create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog_app/blog_list/', cache_page(60)(BlogListView.as_view()), name='blog_list'),
    path('blog_app/blog_detail/<int:pk>/', cache_page(60)(BlogDetailView.as_view()), name='blog_detail'),
    path('blog_app/blog_update/<int:pk>/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog_app/blog_delete/<int:pk>/', BlogDeleteView.as_view(), name='blog_delete'),
]
  