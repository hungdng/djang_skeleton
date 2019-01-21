from django.apps import AppConfig


class ArticlesAppConfig(AppConfig):
    name = 'blog.articles'
    label = 'articles'
    verbose_name = 'Articles'


default_app_config = 'blog.articles.ArticlesAppConfig'
