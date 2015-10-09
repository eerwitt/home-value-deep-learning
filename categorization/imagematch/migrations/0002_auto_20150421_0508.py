# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagematch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(default=None, max_length=15, null=True, help_text=b'Category of image.', choices=[(b'Interior', b'Interior view of a house including bathrooms, living rooms, kitchens or other areas used for indoor socializaing.'), (b'Exterior', b'Exterior view of a house including front, side or rear views.'), (b'Garden', b'A garden, terrace, yard, patio, BBQ, pool, veranda or other outdoor area used for outdoor socializing.'), (b'Land', b'Vacant land or trees which are not part of a living or socializing area.'), (b'View', b'A scenic view of surrounding area or landscape'), (b'Other', b'Other')]),
        ),
    ]
