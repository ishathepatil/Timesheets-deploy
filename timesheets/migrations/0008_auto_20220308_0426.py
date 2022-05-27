# Generated by Django 3.0 on 2022-03-08 09:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0007_auto_20220303_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='master_db',
            name='week_end_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='master_db',
            name='week_start_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]