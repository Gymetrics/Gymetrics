from django.core.management.base import BaseCommand
from dashboard.models import Stream

class Command(BaseCommand):
    def handle(self, *args, **options):
        Stream.objects.all().delete()

        streams = Stream.objects.all().delete()

        bbc = Stream(
            name="BBC One",
            status="g",
            live=True
        )
        
        itv = Stream(
            name="ITV 1",
            status="r",
            live=False
        )

        sky_sports = Stream(
            name="Sky Sports",
            status="a",
            live=True
        )

        mtv = Stream(
            name="ITV 1",
            status="r",
            live=True
        )

        bbc.save()
        itv.save()
        sky_sports.save()
        mtv.save()
