from django.apps import AppConfig


class ArticlesConfig(AppConfig):
    name = 'blog.articles'
    label = 'articles'
    verbose_name = 'Articles'

    def ready(self):
        import blog.articles.signals


default_app_config = 'blog.articles.ArticlesConfig'

from django.apps import AppConfig


# class ArticlesConfig(AppConfig):
#     name = 'blog.authentication'
#     label = 'authentication'
#     verbose_name = 'Authentication'

#     def ready(self):
#         import blog.authentication.signals


# default_app_config = 'blog.authentication.AuthenticationAppConfig'
