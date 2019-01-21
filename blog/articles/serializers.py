from rest_framework import serializers
from .models import Article


class ArticleSerializer(serializers.ModelSerializer):

    # Django REST Framework makes it possible to create a read-only field that
    # gets it's value by calling a function. In this case, the client expects
    # `created_at` to be called `createdAt` and `updated_at` to be `updatedAt`.
    # `serializers.SerializerMethodField` is a good way to avoid having the
    # requirements of the client leak into our API.
    createdDate = serializers.SerializerMethodField(
        method_name='get_created_date')
    updatedDate = serializers.SerializerMethodField(
        method_name='get_updated_date')

    class Meta:
        model = Article
        fields = (
            'content',
            'createdDate',
            'description',
            'title',
            'updatedDate',
            'short_description',
        )

    # See more: https://www.django-rest-framework.org/api-guide/serializers/#saving-instances
    def create(self, validated_data):
        article = Article.objects.create(**validated_data)
        return article

    def get_created_date(self, instance):
        return instance.created_date.isoformat()

    def get_updated_date(self, instance):
        return instance.updated_date.isoformat()
