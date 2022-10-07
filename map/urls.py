from django.urls import path, reverse_lazy
from . import views

app_name='map'
urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
    path('comment',
        views.CommentCreateView.as_view(), name='map_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('map')), name='map_comment_delete'),
]
