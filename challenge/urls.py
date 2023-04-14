from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'challenge'

urlpatterns = [
    path('main/', views.view_main, name='challenge_detail'),
    path('challenge/posting/', views.view_posting_challenge,
         name='view_posting_challenge'),
    path('api/challenge/', views.posting_challenge, name='posting_challenge'),
    path('challenge/<int:id>', views.challenge_detail, name='challenge_detail'),
    path('search_results/', views.challenge_search_view, name='search-results'),
]
