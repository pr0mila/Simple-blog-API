from rest_framework.routers import SimpleRouter

from blogapp.views import PostViewSet, PostTypeViewSet

blog_router = SimpleRouter()
blog_router.register('categories', PostTypeViewSet)
blog_router.register('posts', PostViewSet)