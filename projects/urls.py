from django.urls import path, reverse_lazy
from . import views

app_name = 'projects'
urlpatterns = [
    path('map', views.MapView.as_view(), name='map'),
    path('map/comment',
         views.MapCommentCreateView.as_view(), name='map_comment_create'),
    path('map/comment/<int:pk>/delete',
         views.MapCommentDeleteView.as_view(success_url=reverse_lazy('map')), name='map_comment_delete'),
]
