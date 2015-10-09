from django.db import models


class Image(models.Model):
    zillow_id = models.CharField(
        max_length=15,
        help_text="The Zillow ID from the original JSON.")
    category = models.CharField(
        max_length=15,
        choices=(
            ('Interior', 'Interior'),
            ('Exterior', 'Exterior'),
            ('Garden', 'Garden'),
            ('Land', 'Land'),
            ('Map', 'Map'),
            ('FloorPlan', 'FloorPlan'),
            ('View', 'View'),
            ('Other', 'Other'),
        ),
        null=True,
        default=None,
        help_text="Category of image.")
    url = models.URLField(
        help_text="Image URL to display.")
