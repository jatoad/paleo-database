# Generated by Django 3.2.19 on 2023-07-24 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('museum', '0004_auto_20230719_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='specimen',
            name='slug',
            field=models.SlugField(default='latin_name', max_length=200, unique=True),
        ),
    ]
