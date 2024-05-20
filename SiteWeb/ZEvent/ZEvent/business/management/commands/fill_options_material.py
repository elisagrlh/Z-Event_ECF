from django.core.management.base import BaseCommand
from business.models import OptionsMaterial

class Command(BaseCommand):
    help = 'Fills the OptionsMaterial table with default data'

    def handle(self, *args, **options):
        OptionsMaterial.objects.all().delete()
        materials = [
            {'label': 'Souris', 'brand': 'Razer'},
            {'label': 'Souris', 'brand': 'MSI'},
            {'label': 'Souris', 'brand': 'Logitech'},
            {'label': 'Clavier', 'brand': 'Razer'},
            {'label': 'Clavier', 'brand': 'MSI'},
            {'label': 'Clavier', 'brand': 'Logitech'},
            {'label': 'Moniteur', 'brand': 'Omen'},
            {'label': 'Moniteur', 'brand': 'Samsung'},
            {'label': 'Casque', 'brand': 'JBL'},
            {'label': 'Casque', 'brand': 'HyperX'},
        ]

        for material in materials:
            obj, created = OptionsMaterial.objects.get_or_create(label=material['label'], brand=material['brand'])
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added material: {material["label"]} by {material["brand"]}'))
            else:
                self.stdout.write(self.style.NOTICE(f'Material {material["label"]} by {material["brand"]} already exists.'))
