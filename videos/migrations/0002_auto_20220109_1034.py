# Generated by Django 2.2.24 on 2022-01-09 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='youtube_video',
            name='date_published',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='youtube_video',
            name='name',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
