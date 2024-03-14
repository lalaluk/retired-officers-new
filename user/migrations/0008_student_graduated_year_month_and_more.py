# Generated by Django 5.0.2 on 2024-03-14 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='graduated_year_month',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='student',
            name='military_service_years_int',
            field=models.IntegerField(default=0),
        ),
    ]
