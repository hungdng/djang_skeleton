from django.apps import AppConfig


class AuthenticationAppConfig(AppConfig):
    name = 'blog.authentication'
    label = 'authentication'
    verbose_name = 'Authentication'

    def ready(self):
        import blog.authentication.signals


default_app_config = 'blog.authentication.AuthenticationAppConfig'
