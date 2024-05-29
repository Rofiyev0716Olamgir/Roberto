from django.urls import path

from .views import (
    BlogListView,
    blogdetail,
    LikeRedirectView
)

app_name = 'blog'

urlpatterns = [
    path('blog_list/', BlogListView.as_view(), name='blog_list'),
    path('blog_detail/<slug:slug>/', blogdetail, name='blog_detail'),
    path('blog_lake/<int:eid>', LikeRedirectView.as_view(), name='comment_lake')
]
