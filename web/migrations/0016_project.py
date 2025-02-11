# Generated by Django 5.1.5 on 2025-02-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_alter_budgetquarter_report_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Aprašymas')),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='project_thumbnails', verbose_name='Nuotrauka')),
                ('project_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Projekto ID')),
            ],
            options={
                'verbose_name': 'Projektas',
                'verbose_name_plural': 'Projektai',
            },
        ),
    ]
