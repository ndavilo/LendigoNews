from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('news.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('newsapi/', include('django.contrib.auth.urls')),
    path('newsapi/', include('newsapi.urls')),
    
]
