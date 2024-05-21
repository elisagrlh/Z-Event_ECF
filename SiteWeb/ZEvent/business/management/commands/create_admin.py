from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates an admin user'

    def handle(self, *args, **options):
        if not User.objects.filter(username="elisa").exists():
            User.objects.create_superuser("elisa", "elisagerlach17@gmail.com", "user123")
            self.stdout.write(self.style.SUCCESS('Successfully created new admin user'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists.'))