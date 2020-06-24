from django.conf.urls import include, url

from api.views import PostViewSet

from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'post', PostViewSet)

urlpatterns = [
    url(r"^api/", include(router.urls))
]
