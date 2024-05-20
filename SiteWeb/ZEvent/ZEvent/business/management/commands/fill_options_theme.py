from django.core.management.base import BaseCommand
from business.models import OptionsTheme

class Command(BaseCommand):
    help = 'Fills the OptionsTheme table with default data'

    def handle(self, *args, **options):
        OptionsTheme.objects.all().delete()
        themes = [
            {'name': 'Adventure'},
            {'name': 'Action'},
            {'name': 'MMO'},
            {'name': 'Multijoueur'},
            {'name': 'FPS'},
            {'name': 'RPG'},
    ]

        for theme in themes:
            obj, created = OptionsTheme.objects.get_or_create(name=theme['name'])
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added theme: {theme["name"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Theme {theme["name"]} already exists.'))