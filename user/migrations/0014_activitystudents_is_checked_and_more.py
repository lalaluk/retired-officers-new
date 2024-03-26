# Generated by Django 5.0.2 on 2024-03-21 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_alter_student_graduated_year_month'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitystudents',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activitystudents',
            name='is_get_print',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='activitystudents',
            name='join_number',
            field=models.IntegerField(default=1300),
            preserve_default=False,
        ),
    ]