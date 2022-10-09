from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    path('map', views.MapView.as_view(), name='map'),
    path('map/comment', views.MapCommentCreateView.as_view(), name='map_comment_create'),
    path('map/comment/<int:pk>/delete', views.MapCommentDeleteView.as_view(), name='map_comment_delete'),

    path('bot', views.BotView.as_view(), name='bot'),
    path('bot/comment', views.BotCommentCreateView.as_view(), name='bot_comment_create'),
    path('bot/comment/<int:pk>/delete', views.BotCommentDeleteView.as_view(), name='bot_comment_delete'),

    path('cosmic', views.CosmicPanelView.as_view(), name='cosmic'),
    path('cosmic/comment', views.CosmicCommentCreateView.as_view(), name='cosmic_comment_create'),
    path('cosmic/comment/<int:pk>/delete', views.CosmicCommentDeleteView.as_view(), name='cosmic_comment_delete'),

    path('data_project', views.DataProjectView.as_view(), name="data_project"),
    path('data_project/comment', views.DataProjectCommentCreateView.as_view(), name='data_project_comment_create'),
    path('data_project/comment/<int:pk>/delete', views.DataProjectCommentDeleteView.as_view(), name='data_project_comment_delete'),
]
