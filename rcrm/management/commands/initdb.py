from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand


class Command(BaseCommand):
    SUPER_EMAIL = 'admin@localhost'
    SUPER_PASSWORD = 'secret'

    def handle(self, *args, **options):
        if settings.DEBUG is False:
            self.stderr.write(self.style.ERROR("You must enable DEBUG mode to run this command."))
            return

        if not get_user_model().objects.filter(email=self.SUPER_EMAIL).exists():
            get_user_model().objects.create_superuser(email=self.SUPER_EMAIL, password=self.SUPER_PASSWORD)
            self.stdout.write(self.style.HTTP_SUCCESS("Super user is created."))
            self.stdout.write(self.style.WARNING("\t   email: {}".format(self.SUPER_EMAIL)))
            self.stdout.write(self.style.WARNING("\tpassword: {}".format(self.SUPER_PASSWORD)))
        else:
            self.stdout.write(self.style.NOTICE("Super user already exists. Skipped."))
