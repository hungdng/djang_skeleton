from django.apps import AppConfig


class ProfileAppConfig(AppConfig):
    name = 'blog.profiles'
    label = 'profiles'
    verbose_name = 'Profiles'


default_app_config = 'blog.profiles.ProfileAppConfig'
