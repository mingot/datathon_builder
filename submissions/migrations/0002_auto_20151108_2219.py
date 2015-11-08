# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='docfile',
            new_name='submissionfile',
        ),
        migrations.AlterField(
            model_name='submission',
            name='auc',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
