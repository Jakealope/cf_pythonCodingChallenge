# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Created'),
            preserve_default=True,
        ),
    ]
