# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagematch', '0002_auto_20150421_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='category',
            field=models.CharField(default=None, max_length=15, null=True, help_text=b'Category of image.', choices=[(b'Interior', b'Interior'), (b'Exterior', b'Exterior'), (b'Garden', b'Garden'), (b'Land', b'Land'), (b'Map', b'Map'), (b'FloorPlan', b'FloorPlan'), (b'View', b'View'), (b'Other', b'Other')]),
        ),
    ]
