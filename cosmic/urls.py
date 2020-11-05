from django.urls import path, reverse_lazy
from . import views

app_name='cosmic'
urlpatterns = [
    path('', views.PanelView.as_view(), name='panel'),
    path('comment',
        views.CommentCreateView.as_view(), name='panel_comment_create'),
    path('comment/<int:pk>/delete',
        views.CommentDeleteView.as_view(success_url=reverse_lazy('panel')), name='panel_comment_delete'),
]
