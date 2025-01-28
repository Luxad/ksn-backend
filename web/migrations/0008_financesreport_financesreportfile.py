# Generated by Django 5.1.5 on 2025-01-28 09:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_budgetreport_budgetreportfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FinancesReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Pavadinimas')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Sukurta')),
            ],
            options={
                'verbose_name': 'Finansų ataskaita',
                'verbose_name_plural': 'Finansų ataskaitos',
            },
        ),
        migrations.CreateModel(
            name='FinancesReportFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='finances_reports', verbose_name='Failas')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='web.financesreport')),
            ],
            options={
                'verbose_name': 'Failas',
                'verbose_name_plural': 'Failai',
            },
        ),
    ]
