from django.urls import path

from .views import PostListView,PostDetailView ,CommentListView

app_name="post"


urlpatterns = [
    path('postlist/', PostListView.as_view(), name="post_list"),
    path('postlist/<int:pk>/', PostDetailView.as_view(), name="post_detail"),

    path('postlist/<int:pk>/comment/', CommentListView.as_view(), name="comment_list"),

]