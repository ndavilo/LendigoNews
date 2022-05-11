from django.urls import include, path
from .views import PostViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'NewsApi', PostViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework')),
]