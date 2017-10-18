from django.conf.urls import include, url
from rest_framework import routers

from core.views import ReviewViewSet, CategoryViewSet, PlaceListView

router = routers.DefaultRouter()
router.register(r'reviews', ReviewViewSet, 'reviews')
router.register(r'categories', CategoryViewSet, 'categories')

urlpatterns = [
    url(r'^places/$', PlaceListView.as_view(), name='placesList'),
    url(r'^auth/', include('authentication.urls')),
    url(r'^', include(router.urls), name='api-root'),
    url(r'^', include('friends.urls'), name='friends')
]
