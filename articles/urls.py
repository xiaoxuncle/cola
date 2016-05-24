from django.conf.urls import url

from articles.views import add_article, article

urlpatterns = [
    url(r'^add$', add_article),
    url(r'(\d+)', article)
]