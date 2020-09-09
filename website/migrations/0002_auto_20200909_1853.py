# Generated by Django 3.1.1 on 2020-09-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movieitem',
            name='imdb_id',
            field=models.CharField(db_index=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='movieitem',
            name='type',
            field=models.CharField(blank=True, choices=[('movie', 'movie'), ('series', 'series'), ('episode', 'episode')], max_length=7),
        ),
        migrations.AlterField(
            model_name='movieitem',
            name='year',
            field=models.IntegerField(blank=True),
        ),
    ]