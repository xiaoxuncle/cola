from django.conf.urls import url, include
from django.contrib import admin

import articles
from articles.views import index, add_article
from authentication.views import user

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^articles/', include('articles.urls')),
    url(r'^auth/', include('authentication.urls')),
    url(r'^people/(\w+)', user)
]
