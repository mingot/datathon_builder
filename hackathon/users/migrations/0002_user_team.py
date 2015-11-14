# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='team',
            field=models.CharField(blank=True, max_length=2, null=True, choices=[('01', 'The G-Priors'), ('02', 'TeamUNO'), ('03', 'Pretty fly for a wifi'), ('04', 'Multimetro'), ('05', 'Hacaguays'), ('06', 'Bcn R users group'), ('07', 'Alpha'), ('08', 'Red Jaguars'), ('09', 'Silver Snakes'), ('10', 'Green Monkeys')]),
        ),
    ]
