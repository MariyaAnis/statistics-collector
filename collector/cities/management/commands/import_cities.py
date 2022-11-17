import csv
import logging
import os

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from cities.models import City

logging.basicConfig(
    level=logging.INFO,
    filename='main.log',
    format='%(asctime)s, %(levelname)s, %(name)s, %(message)s',
    filemode='w',
)

DATA_ROOT = os.path.join(settings.BASE_DIR, 'data')


class Command(BaseCommand):
    help = 'Load data from csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('filename', default='Cities.csv', nargs='?',
                            type=str)

    def handle(self, *args, **options):
        try:
            with open(
                    os.path.join(DATA_ROOT, options['filename']),
                    newline='',
                    encoding='utf8'
            ) as csv_file:
                data = csv.reader(csv_file)
                for row in data:
                    idd, name, country, lat, lon = row
                    City.objects.get_or_create(
                        name=name,
                        country=country,
                        lat=lat,
                        lon=lon,
                    )
        except FileNotFoundError:
            raise CommandError('Добавьте файл Cities в директорию data')
        logging.info('Successfully loaded all data into database')
