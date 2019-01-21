from django.db import models
from django.db.models import Count, Avg
from core.models.model_abstract import TimestampedModel

from django.core.validators import MinLengthValidator

import uuid


class ArticleQuerySet(models.QuerySet):
    def avarage(self):
        return self.annotate(Count('avarage'))\
            .order_by('avarage__count')

    def newest(self):
        return self.order_by('-created_at')


class Article(TimestampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(db_index=True, max_length=255, validators=[
                             MinLengthValidator(3)])
    description = models.TextField()
    content = models.TextField()
    short_description = models.TextField(null=True)

    objects = models.Manager()
    sorted_objects = ArticleQuerySet.as_manager()

    def __str__(self):
        return self.description
