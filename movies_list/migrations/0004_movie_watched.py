# Generated by Django 4.1.3 on 2023-02-10 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_list', '0003_remove_movie_comment_movie_commentary'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watched',
            field=models.BooleanField(default=False),
        ),
    ]