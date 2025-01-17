# Generated by Django 5.1.5 on 2025-01-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_post_image_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='thumbnail',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Trumpas aprašymas'),
        ),
    ]
