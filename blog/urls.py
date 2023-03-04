from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
 
from post.sitemaps import PostSiteMap

sitemaps = {
    'posts': PostSiteMap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    path('post/', include('post.urls', namespace="post")),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap"),

]
