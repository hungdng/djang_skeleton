from rest_framework import serializers, status
from rest_framework.exceptions import NotFound
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, mixins

from .models import Profile
from .serializers import ProfileSerializer, ProfileSerializerUpdate
from rest_framework.decorators import action


class ProfileRetrieveViewSet(viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Profile.objects.select_related('user')
    serializer_class = ProfileSerializer

    def get_serializer_class(self):
        return super().get_serializer_class()
