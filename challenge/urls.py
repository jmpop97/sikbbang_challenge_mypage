from django.urls import path
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
    path('challenge/<int:id>/join/', views.join_challenge, name='join_challenge'),
    path('challenge/<int:id>/complete/',
         views.complete_challenge, name='complete_challenge'),
]
