from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from django.conf import settings
from django.conf.urls.static import static
 
from post.sitemaps import PostSiteMap

sitemaps = {
    'posts': PostSiteMap,
}

urlpatterns = [
    path('admin/', admin.site.urls),

    path('post/', include('post.urls', namespace="post")),

    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name="django.contrib.sitemaps.views.sitemap"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)