from .views import ArticleViewSet, TagViewSet
from rest_framework_nested import routers
from django.urls import include, path
from django.conf.urls import url

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', ArticleViewSet,)

router_tags = routers.SimpleRouter(trailing_slash=False)
router_tags.register(r'', TagViewSet,)

urlpatterns = [
    path('articles/', include(router.urls)),
    path('tags/', include(router_tags.urls)),
]
