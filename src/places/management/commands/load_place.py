from pathlib import Path

import requests
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place


class Command(BaseCommand):
    help = 'Load new place from json file'  # noqa

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        response = requests.get(options['url'])
        response.raise_for_status()
        place_content = response.json()

        place, created = Place.objects.update_or_create(
            title=place_content['title'],
            defaults={
                'short_description': place_content['description_short'],
                'long_description': place_content['description_long'],
                'longitude': place_content['coordinates']['lng'],
                'latitude': place_content['coordinates']['lat'],
            },
        )

        if created:
            place.images.all().delete()

        for sort_order, url in enumerate(place_content['imgs']):
            response = requests.get(url)
            image_content = (ContentFile(response.content))
            place_image = place.images.create(sort_order=sort_order)
            place_image.image.save(name=Path(url).name, content=image_content, save=True)

        self.stdout.write(self.style.SUCCESS(f'Successfully created place "{place}"'))
