# Generated by Django 3.2.2 on 2021-05-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='strefa',
            name='lista_pozycji',
            field=models.JSONField(default={}),
        ),
    ]
