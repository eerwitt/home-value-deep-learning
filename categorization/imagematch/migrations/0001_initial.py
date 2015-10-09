# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('zillow_id', models.CharField(help_text=b'The Zillow ID from the original JSON.', max_length=15)),
                ('category', models.CharField(default=None, max_length=15, null=True, help_text=b'Category of image.', choices=[(b'Exterior', b'Exterior view of a house including front, side or rear views.'), (b'Interior', b'Interior view of a house including bathrooms, living rooms, kitchens or other areas used for indoor socializaing.'), (b'Garden', b'A garden, terrace, yard, patio, BBQ, pool, veranda or other outdoor area used for outdoor socializing.'), (b'Land', b'Vacant land or trees which are not part of a living or socializing area.'), (b'View', b'A scenic view of surrounding area or landscape'), (b'Other', b'Other')])),
                ('url', models.URLField(help_text=b'Image URL to display.')),
            ],
        ),
    ]
