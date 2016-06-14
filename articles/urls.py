from django.conf.urls import url

from articles.views import add_article, article, add_comment

urlpatterns = [
    url(r'^add$', add_article),
    url(r'^(\d+)$', article),
    url(r'^add_comment$', add_comment)
]