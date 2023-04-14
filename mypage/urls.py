from django.urls import path
from . import views   # user/views 불러오기

urlpatterns = [
    path('test1/', views.mychallenge, name='a'),
    path('test2/', views.mychallengeadd, name='b'),
    path('test/', views.mychallengeform, name='c'),
    path('mypage/',views.mypage_list,name='mypage-list')
]