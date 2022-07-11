from django.core.management import BaseCommand
from faker import Faker
from random import randrange

from search.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        faker = Faker()

        for _ in range(50):
            Product.objects.create(
                title=faker.name(),
                image=faker.image_url(),
                description=faker.text(200),
                price=randrange(10, 100)
            )
