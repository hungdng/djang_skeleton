from django.conf.urls import url

from .views import ProfileRetrieveAPIView, ProfileFollowAPIView

urlpatterns = [
    # url(r'^profiles/(?P<username>\w+)/?$', ProfileRetrieveAPIView.as_view()),
]
