# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='author',
            fields=[
                ('authorid', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField(default=18)),
                ('country', models.CharField(default=b'CHINA', max_length=50)),
            ],
            options={
                'db_table': 'author',
            },
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('isbn', models.CharField(max_length=50, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('publishdate', models.DateField(max_length=50)),
                ('price', models.FloatField(max_length=50)),
                ('author', models.ForeignKey(to='lms.author')),
            ],
            options={
                'db_table': 'book',
            },
        ),
    ]
