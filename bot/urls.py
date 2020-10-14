from django.urls import path, reverse_lazy
from . import views

app_name='bot'
urlpatterns = [
    # path('', views.MapView.as_view()),
    path('', views.BotView.as_view(), name='bot'),
    path('comment',
        views.CommentCreateView.as_view(), name='bot_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('bot')), name='bot_comment_delete'),
]
