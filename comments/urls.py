from django.urls import path
from . import views

urlpatterns = [
    # path('api/comments', views.comment_read, name="comment_read"), #mainpage에서 challenge 썸네일 클릭 시 나오는 화면
    path('api/comments', views.comment_create, name="comment_create"),
    # path('api/comments', views.comment_update, name="comment_update"),
    # path('api/comments', views.comment_delete, name="comment_delete"),
]
