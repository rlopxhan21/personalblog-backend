from rest_framework import serializers

from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    active = serializers.BooleanField(read_only=True)

    class Meta:
        model = Comment
        fields = "__all__"


class PostSerializer(serializers.ModelSerializer):
    commented_post = CommentSerializer(many=True, read_only=True)
    active = serializers.BooleanField(read_only=True)
    slug = serializers.SlugField(read_only=True)

    class Meta:
        model = Post
        fields = "__all__"