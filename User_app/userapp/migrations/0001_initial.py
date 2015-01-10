# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('f_name', models.CharField(max_length=100, verbose_name=b'First Name')),
                ('l_name', models.CharField(max_length=200, verbose_name=b'Last Name')),
                ('email', models.EmailField(max_length=75, verbose_name=b'Email')),
                ('create_date', models.DateTimeField(verbose_name=b'Date Created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
