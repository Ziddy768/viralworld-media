from django.urls import path
from . import views

# Ip address:8000/other

urlpatterns = [
    path('', views.simple_view),
    path('other/', views.mock_view),
]