from django.urls import path
from django.conf.urls.static import static  # urlpatterns += 전용
from django.conf import settings  # urlpatterns += 전용
from . import views

app_name = 'challenge_app'

urlpatterns = [
    path('main/', views.view_main, name='view_main'),
    path('challenge/posting/', views.view_posting_challenge,
         name='view_posting_challenge'),
    path('api/challenge/', views.posting_challenge, name='posting_challenge'),
    path('challenge/<int:id>/', views.challenge_detail, name='challenge_detail'),
    path('challenge/<int:id>/delete/',
         views.delete_challenge, name='delete_challenge'),
    path('search_results/', views.challenge_search_view, name='search-results'),
    path('challenge/<int:id>/edit/',
         views.edit_challenge, name='edit_challenge'),
    path('api/comments/edit/<int:id>',
         views.comment_update, name="comment_update"),
    path('api/comments/delete/<int:id>',
         views.comment_delete, name="comment_delete"),
    path('challenge/<int:id>/join/', views.join_challenge, name='join_challenge'),
    path('challenge/<int:id>/complete/',
         views.complete_challenge, name='complete_challenge'),
]
