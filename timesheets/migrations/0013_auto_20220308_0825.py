# Generated by Django 3.0 on 2022-03-08 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('timesheets', '0012_auto_20220308_0736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master_db',
            name='week_end',
            field=models.DateField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='master_db',
            name='week_start',
            field=models.DateField(blank=True, default=django.utils.timezone.now, editable=False),
        ),
    ]
