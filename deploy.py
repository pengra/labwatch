from django.core.management import execute_from_command_line
from django.contrib.auth.models import User
from os import getenv, environ

if __name__ == '__main__':
    # run migrations
    print('[DEPLOY]: settings DJANGO_SETTINGS_MODULE')
    environ.setdefault("DJANGO_SETTINGS_MODULE", "labwatch.settings")
    print('[DEPLOY]: running migrations')
    execute_from_command_line('migrate')
    if User.objects.filter(username=getenv('SUPERUSER_USERNAME', 'qwergram')).count() == 0:
        print('[DEPLOY]: creating superuser')
        user = User(
            username=getenv('SUPERUSER_USERNAME', 'qwergram'),
            password=getenv('SUPERUSER_PASSWORD', 'default_p@ssword'),
            email=getenv('SUPERUSER_EMAIL', 'npengra317@gmail.com'),
        )
        user.save()
