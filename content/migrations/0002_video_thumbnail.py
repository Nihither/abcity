# Generated by Django 4.1.7 on 2024-02-23 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.FileField(default=123, upload_to='thumbnails', verbose_name='Постер'),
            preserve_default=False,
        ),
    ]