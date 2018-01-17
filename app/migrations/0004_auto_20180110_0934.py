# Generated by Django 2.0.1 on 2018-01-10 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_personne'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='prix',
            field=models.FloatField(blank=True, default=0.0),
        ),
        migrations.AddField(
            model_name='produit',
            name='votes',
            field=models.ManyToManyField(blank=True, default=None, to='app.Personne'),
        ),
    ]