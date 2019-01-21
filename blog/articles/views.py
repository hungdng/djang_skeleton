from rest_framework import generics, mixins, status, viewsets
from rest_framework.exceptions import NotFound
# from rest_framework.permissions import (
#     AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
# )
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer
from core import Paginator


class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_class = ArticleSerializer

    def get_queryset(self):
        queryset = self.queryset
        return queryset

    def create(self, request):
        serializer_context = {
            'request': request
        }
        serializer_data = request.data

        serializer = self.serializer_class(
            data=serializer_data, context=serializer_context
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        page_size = self.request.query_params.get("pageSize", 10)
        page = self.request.query_params.get("page", 1)

        serializer_context = {'request': request}
        page = self.paginate_queryset(self.get_queryset())

        serializer = self.serializer_class(
            page,
            context=serializer_context,
            many=True
        )

        return self.get_paginated_response(serializer.data)
