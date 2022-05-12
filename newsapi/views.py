from news.models import Post
from rest_framework import viewsets
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all().order_by('-id')
	serializer_class = PostSerializer
