from rest_framework import viewsets

from blogapp.models import PostType, Post
from blogapp.serializer import PostTypeSerializer, PostSerializer


class PostTypeViewSet(viewsets.ModelViewSet):
    serializer_class = PostTypeSerializer
    queryset = PostType.objects.all()


class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
