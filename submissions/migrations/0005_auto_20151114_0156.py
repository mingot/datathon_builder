# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import submissions.models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0004_auto_20151110_0139'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='file_error',
            field=models.TextField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submissionfile',
            field=models.FileField(upload_to=submissions.models.update_filename),
        ),
    ]
