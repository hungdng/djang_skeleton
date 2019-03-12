from django.conf.urls import url
from django.urls import include, path
from rest_framework_nested.routers import (
    DefaultRouter,
    SimpleRouter
)

from .views import UserViewSet

router = SimpleRouter(trailing_slash=False)
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('registration', RegistrationViewSet.as_view(
    #     {'post': 'create_user'}), name='registration'),
    # path('login', LoginViewSet.as_view({'post': 'login'}), name='login'),
]
