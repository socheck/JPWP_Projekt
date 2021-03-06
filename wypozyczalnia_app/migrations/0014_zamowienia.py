# Generated by Django 3.2 on 2021-05-20 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wypozyczalnia_app', '0013_alter_hulajnoga_czy_wynajety'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zamowienia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_usera', models.IntegerField()),
                ('kwota', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('nr_karty', models.CharField(blank=True, max_length=16, null=True)),
                ('rodzaj_pojazdu', models.CharField(choices=[('h', 'hulajnoga'), ('s', 'samochód')], default='s', max_length=30)),
                ('typ_wynajmu', models.CharField(choices=[('d', 'długoterminowy'), ('k', 'krótkoterminowy')], default='k', max_length=30)),
                ('id_pojazdu', models.IntegerField()),
                ('czas_startu', models.DateTimeField(default=None)),
                ('czas_koniec', models.DateTimeField(blank=True, default=None, null=True)),
                ('czy_obecnie_wynajety', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Zamuwienie',
                'verbose_name_plural': 'Zamówienia',
            },
        ),
    ]
