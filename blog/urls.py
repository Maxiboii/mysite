from django.urls import path, reverse_lazy
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.PostsView.as_view(), name='blog'),
    path('post/<_id>/', views.PostView.as_view(), name='post'),
    path('comment',
        views.CommentCreateView.as_view(), name='blog_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('blog')), name='blog_comment_delete'),
]
