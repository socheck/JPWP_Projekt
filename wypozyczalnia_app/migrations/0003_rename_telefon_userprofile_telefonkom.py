# Generated by Django 3.2.2 on 2021-05-08 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia_app', '0002_alter_userprofile_telefon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='telefon',
            new_name='telefonkom',
        ),
    ]
