from django.urls import path

from .views import PostListView,PostDetailView ,CommentListView

app_name="post"



urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('<int:pk>/', PostDetailView.as_view(), name="post_detail"),

    path('<int:pk>/comment/', CommentListView.as_view(), name="comment_list"),
]