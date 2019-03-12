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
        if self.action == 'update_profile':
            return ProfileSerializerUpdate
        if self.action == 'retrieve_profile':
            return ProfileSerializer
        return super().get_serializer_class()

    @action(detail=False, methods=['get'], url_path='me')
    def retrieve_profile(self, request, *args, **kwargs):
        try:
            profile = self.queryset.get(user__username=request.user.username)
        except Profile.DoesNotExist:
            raise NotFound('A profile with this username does not exist.')

        serializer = self.serializer_class(profile)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @retrieve_profile.mapping.patch
    def update_profile(self, request, *args, **kwargs):
        user_data = request.data

        serializer_data = {
            'username': user_data.get('username', request.user.username),
            'email': user_data.get('email', request.user.email),

            'profile': {
                'bio': user_data.get('bio', request.user.profile.bio),
                'image': user_data.get('image', request.user.profile.image)
            }
        }

        serializer = self.serializer_class(
            request.user, data=serializer_data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        # serializer_data = {
        #     'username': serializer.instance.username,
        #     'bio': serializer.instance.bio,
        #     'image': serializer.instance.image
        # }

        return Response(serializer.data, status=status.HTTP_200_OK)
