from django.urls import path
from challenge import views

urlpatterns = [
    path('', views.posting, name='post_challenge'),
]
