from django.conf.urls import include, url
from . import views


urlpatterns = [

    url(r'^', include('djoser.urls.authtoken')),

]
