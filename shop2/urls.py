from django.urls import path, re_path, include
from django.contrib import admin


urlpatterns = [
    path('', include("main.urls")),
    path('admin/', admin.site.urls, name="admin"),
]