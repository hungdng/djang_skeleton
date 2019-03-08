from django.conf.urls import url
from django.urls import include, path
from rest_framework_nested.routers import (
    DefaultRouter,
    SimpleRouter
)

from .views import (
    LoginAPIView, RegistrationAPIView, UserViewSet
)

# from .views import (UserViewSet)

router = SimpleRouter(trailing_slash=False)
# router.register(r'user', UserViewSet, 'user')

urlpatterns = [
    # path('', include(router.urls)),
    path('registration', RegistrationAPIView.as_view(
        {'post': 'create_user'}), name='registration'),
    # url(r'^users/login/?$', LoginAPIView.as_view()),
]
