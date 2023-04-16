from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('qna_list/', views.qna_list_view, name='qna_list'),
    path('qna/create/', views.qna_create_view, name='qna-create'),
    path('qna/detail/<int:pk>/', views.qna_detail_view, name='qna-detail'),
    path('qna/edit/<int:pk>/', views.qna_edit_view, name='qna-edit'),
    path('qna/delete/<int:pk>/', views.qna_delete_view, name='qna-delete')
]
