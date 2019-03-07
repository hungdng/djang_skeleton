from django.conf.urls import url
from django.urls import include, path
from rest_framework_nested import routers

# from .views import (
#     LoginAPIView, RegistrationAPIView, UserViewSet
# )

from .views import (UserViewSet)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, base_name='users')

urlpatterns = [
    path('', include(router.urls)),
    # url(r'^users/?$', RegistrationAPIView.as_view()),
    # url(r'^users/login/?$', LoginAPIView.as_view()),
]
