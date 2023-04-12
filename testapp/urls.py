from django.urls import path
from django.contrib import admin
from . import views   # user/views 불러오기

urlpatterns = [
    path('', admin.site.urls),
]