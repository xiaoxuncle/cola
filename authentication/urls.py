from django.conf.urls import url

from authentication.views import signin, logout

urlpatterns = [
    url(r'^signin/', signin),
    url(r'^logout/',logout)
]
