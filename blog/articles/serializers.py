from rest_framework import serializers

from .models import Article, Tag

from blog.profiles.serializers import ProfileSerializer
from .relations import TagRelatedField


class ArticleSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    description = serializers.CharField(required=False)
    slug = serializers.SlugField(required=False)

    tag_list = TagRelatedField(many=True, required=False, source='tags')

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
            'author',
            'body',
            'createdDate',
            'description',
            'slug',
            'tag_list',
            'title',
            'updatedDate',
        )

    def create(self, validated_data):
        author = self.context.get('author', None)

        tags = validated_data.pop('tags', [])

        article = Article.objects.create(author=author, **validated_data)

        for tag in tags:
            article.tags.add(tag)

        return article

    def get_created_date(self, instance):
        return instance.created_date.isoformat()

    def get_updated_date(self, instance):
        return instance.updated_date.isoformat()


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

    def to_representation(self, obj):
        return obj.tag
