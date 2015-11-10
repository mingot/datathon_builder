# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0003_auto_20151108_2303'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submission',
            old_name='auc',
            new_name='auc_private',
        ),
        migrations.AddField(
            model_name='submission',
            name='auc_public',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
