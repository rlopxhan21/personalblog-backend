from django.db import models

from django.contrib.auth.models import User

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)

class Post(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField(max_length=256)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    active= models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = ActiveManager()

    class Meta:
        ordering = ['-updated']
        indexes = [
            models.Index(fields=['-updated'])
        ]

    def __str__(self):
        return self.title

class Comment(models.Model):
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="commented_post")
    active= models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    published = ActiveManager()

    def __str__(self):
        return self.body

