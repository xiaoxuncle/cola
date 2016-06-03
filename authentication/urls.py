from django.conf.urls import url

from authentication.views import signin, logout, signup

urlpatterns = [
    url(r'^signin/', signin),
    url(r'^logout/',logout),
    url(r'^signup/', signup)
]
