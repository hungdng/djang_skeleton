from .views import ProfileRetrieveViewSet
from rest_framework_nested import routers
from django.urls import include, path
from django.conf.urls import url

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'', ProfileRetrieveViewSet,)

urlpatterns = [
    path('', include(router.urls)),
    # path('<username>', ProfileRetrieveViewSet.as_view(
    #     {'get': 'retrieve_profile'}), name='retrieve_profile'),
    # path('update/<username>', ProfileRetrieveViewSet.as_view(
    #     {'patch': 'update_profile'}), name='update_profile'),
]
