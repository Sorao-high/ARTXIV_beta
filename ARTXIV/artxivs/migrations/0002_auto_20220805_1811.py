# Generated by Django 3.1.2 on 2022-08-05 09:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('artxivs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artxiv',
            name='family_name',
        ),
        migrations.RemoveField(
            model_name='artxiv',
            name='first_name',
        ),
        migrations.AddField(
            model_name='artxiv',
            name='artist_name',
            field=models.CharField(default=datetime.datetime(2022, 8, 5, 9, 11, 1, 759550, tzinfo=utc), max_length=20, verbose_name='Artist name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='artxiv',
            name='contributor_name',
            field=models.CharField(default=datetime.datetime(2022, 8, 5, 9, 11, 11, 551399, tzinfo=utc), max_length=20, verbose_name='Contributor name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='artxiv',
            name='abstract',
            field=models.CharField(max_length=1000, verbose_name='Abstract'),
        ),
    ]
