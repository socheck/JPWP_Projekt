# Generated by Django 3.2.2 on 2021-05-15 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia_app', '0010_typauta_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='samochod',
            name='kod',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
