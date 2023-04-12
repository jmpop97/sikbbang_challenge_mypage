from django.urls import path
from . import views   # user/views 불러오기

urlpatterns = [
    path('test/', views.mychallenge, name='a'),
]