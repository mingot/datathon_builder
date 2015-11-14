# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='team',
            field=models.CharField(max_length=50, null=True, blank=True),
        ),
    ]
