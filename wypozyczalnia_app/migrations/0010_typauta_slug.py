# Generated by Django 3.2.2 on 2021-05-13 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia_app', '0009_merge_20210509_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='typauta',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
    ]
