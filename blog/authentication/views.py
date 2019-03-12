from rest_framework import status, viewsets, mixins
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from .serializers import (
    LoginSerializer, RegistrationSerializer, UserSerializer
)

from rest_framework.decorators import action
from .models import User


class UserViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    queryset = User.objects.select_related('profile')

    def get_serializer_class(self):
        if self.action == 'login':
            return LoginSerializer
        if self.action == 'create_user':
            return RegistrationSerializer
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
        user_data = request.data

        serializer_data = {
            'username': user_data.get('username', request.user.username),
            'password': user_data.get('password', None),
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

        return Response(serializer.data, status=status.HTTP_200_OK)
