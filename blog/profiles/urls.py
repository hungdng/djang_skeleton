from .views import ProfileRetrieveViewSet
from rest_framework_nested.routers import (
    DefaultRouter,
    SimpleRouter
)
from django.urls import include, path
from django.conf.urls import url

urlpatterns = [
    path('<username>', ProfileRetrieveViewSet.as_view(
        {'get': 'retrieve_profile'}), name='retrieve_profile'),
    path('update/<username>', ProfileRetrieveViewSet.as_view(
        {'patch': 'update_profile'}), name='update_profile'),
]
