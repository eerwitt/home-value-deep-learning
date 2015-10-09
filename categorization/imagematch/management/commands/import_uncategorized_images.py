from django.core.management.base import BaseCommand
import csv

from imagematch.models import Image


class Command(BaseCommand):
    args = "<uncategorized images input TSV (zillow_id\turl)>"
    help = """
    Create Images for all the uncategorized images in a TSV.
    """

    def handle(self, *args, **options):
        args_list = list(args)
        input_filename = args_list.pop(0)

        with open(input_filename, "r") as input_file:
            reader = csv.DictReader(
                input_file,
                delimiter="\t")

            for row in reader:
                Image.objects.create(
                    zillow_id=row["zillow_id"],
                    url=row["url"])
