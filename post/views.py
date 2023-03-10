from rest_framework import mixins,generics
from rest_framework_api_key.permissions import HasAPIKey

from .serializers import PostSerializer, CommentSerializer
from .models import Post, Comment
from .pagination import StandardPagination

class PostListView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = [HasAPIKey]
    pagination_class = StandardPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
class PostDetailView(mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset = Post.published.all()
    serializer_class = PostSerializer
    permission_classes = [HasAPIKey]


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    
class CommentListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    serializer_class = CommentSerializer
    permission_classes = [HasAPIKey]


    def get_queryset(self, *args, **kwargs):
        pk = self.kwargs['pk']
        return Comment.published.filter(post_id=pk)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)