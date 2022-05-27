from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUbdateView,
    BlogDaleteView,
)

urlpatterns = [
    path('post/<int:pk>/delete/',BlogDaleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit',BlogUbdateView.as_view(), name='post_edit'),
    path('post/new/',BlogCreateView.as_view(), name='post_new'),
    path('',BlogListView.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(), name='post_detail'),
]