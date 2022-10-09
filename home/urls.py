from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('data_project/', views.DataProjectView.as_view(), name="data_project"),
]
