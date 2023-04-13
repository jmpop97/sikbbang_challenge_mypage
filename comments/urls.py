from django.urls import path
from . import views
from django.conf.urls.static import static #urlpatterns += 전용
from django.conf import settings #urlpatterns += 전용

urlpatterns = [
    path('api/comments', views.comment_read, name="comment_read"), #mainpage에서 challenge 썸네일 클릭 시 나오는 화면
    path('api/comments/create', views.comment_create, name="comment_create"),
    # path('api/comments', views.comment_update, name="comment_update"),
    # path('api/comments', views.comment_delete, name="comment_delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #장고한테 이미지 루트를 알려줌