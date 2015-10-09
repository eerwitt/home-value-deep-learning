from django.core.management.base import BaseCommand
import csv

from imagematch.models import Image


class Command(BaseCommand):
    args = "<training TSV output filename>"
    help = """
    Generate a TSV used for training in Caffe based on categorized images.

    NOTE does no pagination, if you are doing a ton of images then try using
    something from the database engine.

    For instance:
        psql:
            `\copy (select zillow_id, url, category from imagematch_image);`
    """

    def handle(self, *args, **options):
        args_list = list(args)
        output_filename = args_list.pop(0)

        with open(output_filename, "w") as output_file:
            writer = csv.DictWriter(
                output_file,
                delimiter="\t",
                fieldnames=["zillow_id", "url", "category"])
            writer.writeheader()

            for image in Image.objects.exclude(category__isnull=True):
                writer.writerow(
                    {
                        "zillow_id": image.zillow_id,
                        "url": image.url,
                        "category": image.category
                    })
