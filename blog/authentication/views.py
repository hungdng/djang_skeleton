from rest_framework import status, viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer, UserSerializerRetrieve
)

from rest_framework.decorators import action
from .models import User
from blog.profiles.models import Profile
from rest_framework.exceptions import NotFound
from .Permissions import IsUserPermission, IsAdminPermission


class UserViewSet(viewsets.GenericViewSet, mixins.RetrieveModelMixin, mixins.ListModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.select_related('profile')

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve' or self.action == 'partial_update' or self.action == 'get_me' or self.action == 'update_me':
            permission_classes = [IsAdminPermission, ]
        elif self.action == 'login' or self.action == 'create_user':
            permission_classes = [AllowAny, ]
        else:
            permission_classes = [IsUserPermission, ]
        return [permission() for permission in permission_classes]

    def get_serializer_class(self):
        if self.action == 'list':
            return UserSerializer
        if self.action == 'retrieve':
            return UserSerializerRetrieve
        return super().get_serializer_class()

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        user = request.data

        serializer = LoginSerializer(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'], url_path='registration')
    def create_user(self, request):
        user = request.data

        serializer = RegistrationSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        user = self.get_object()
        return Response(self.update_user(request.data, user), status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'], url_path='me')
    def get_me(self, request, *args, **kwargs):
        # return super().retrieve(request, *args, **kwargs)

        serializer = self.serializer_class(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @get_me.mapping.put
    def update_me(self, request, *args, **kwargs):
        return Response(self.update_user(request.data, request.user), status=status.HTTP_200_OK)

    # Function Update user
    def update_user(self, user_data, user):
        serializer_data = {
            'username': user_data.get('username', user.username),
            'password': user_data.get('password', None),
            'profile': {
                'bio': user_data.get('bio', user.profile.bio),
                'image': user_data.get('image', user.profile.image)
            }
        }

        serializer = UserSerializer(
            user, data=serializer_data, partial=True,
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return serializer.data
