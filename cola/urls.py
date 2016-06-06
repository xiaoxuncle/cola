from django.conf.urls import url, include
from django.contrib import admin

import articles
from articles.views import index, add_article

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    url(r'^articles/', include('articles.urls')),
    url(r'^auth/', include('authentication.urls')),
]
