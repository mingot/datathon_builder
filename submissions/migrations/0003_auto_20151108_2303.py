# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0002_auto_20151108_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='submissionfile',
            field=models.FileField(upload_to=b'documents/'),
        ),
        migrations.AlterField(
            model_name='submission',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
