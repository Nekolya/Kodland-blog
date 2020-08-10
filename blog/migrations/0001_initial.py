# Generated by Django 3.0.8 on 2020-08-10 10:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('creation_date', models.DateField(default=datetime.datetime(2020, 8, 10, 10, 8, 24, 573374, tzinfo=utc))),
                ('text', models.TextField(blank=True, max_length=10000)),
            ],
        ),
    ]
