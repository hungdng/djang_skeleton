from django.conf.urls import include, url
from django.urls import path

from rest_framework.routers import DefaultRouter

from .views import (
    ArticleViewSet,
)

router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet, base_name='articles')

urlpatterns = [
    url(r'^', include(router.urls))
]
