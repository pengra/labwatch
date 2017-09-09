#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "labwatch.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    if (sys.argv[1]) == 'autocreatesuperuser':
        from django.contrib.auth.models import User
        User.objects.filter(email=os.environ['SUPERUSER_EMAIL']).delete()
        User.objects.create_superuser(
            os.environ['SUPERUSER_USERNAME'],
            os.environ['SUPERUSER_EMAIL'],
            os.environ['SUPERUSER_PASSWORD']
        )
    elif (sys.argv[1]) == 'autocreategroups':
        from django.contrib.auth.models import Group
        if len(Group.objects.filter(name='Engineer')) == 0:
            Group('Engineer').save()
        if len(Group.objects.filter(name='Librarian')) == 0:
            Group('Librarian').save()
        if len(Group.objects.filter(name='Teacher')) == 0:
            Group('Teacher').save()
    else:
        execute_from_command_line(sys.argv)
