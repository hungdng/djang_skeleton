from rest_framework import permissions
from django.contrib.auth.models import AnonymousUser


class IsUserPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        return request.user.is_staff is not True


class IsAdminPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if isinstance(request.user, AnonymousUser):
            return False
        return request.user.is_staff is True
