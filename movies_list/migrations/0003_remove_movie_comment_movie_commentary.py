# Generated by Django 4.1.3 on 2023-02-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0002_remove_movie_watched_movie_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='comment',
        ),
        migrations.AddField(
            model_name='movie',
            name='commentary',
            field=models.CharField(default='good movie', max_length=30),
            preserve_default=False,
        ),
    ]