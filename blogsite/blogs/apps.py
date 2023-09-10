from django.apps import AppConfig

from django.contrib.auth.signals import user_logged_in


def my_callback(sender, **kwargs):
    request = kwargs['request']
    user = kwargs['user']
    ip = request.META.get('REMOTE_ADDR')
    from .models import User
    User.objects.filter(username=user).update(ip=ip)

class BlogsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blogs'

    def ready(self):
        user_logged_in.connect(my_callback)

