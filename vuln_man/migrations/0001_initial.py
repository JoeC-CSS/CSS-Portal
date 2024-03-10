# Generated by Django 5.0.3 on 2024-03-10 11:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VulnItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vuln_name', models.CharField(max_length=100)),
                ('risk_level', models.CharField(max_length=100)),
                ('affected_assets', models.CharField(max_length=100)),
                ('date_added', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]