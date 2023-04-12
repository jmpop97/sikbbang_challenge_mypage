from django.urls import path
from . import views   # user/views 불러오기

urlpatterns = [
    path('test1/', views.mychallenge, name='a'),
    path('test/', views.mychallengeadd, name='a'),
]