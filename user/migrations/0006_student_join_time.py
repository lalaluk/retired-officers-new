# Generated by Django 5.0.2 on 2024-03-12 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_student_military_type_student_notes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='join_time',
            field=models.DateTimeField(null=True),
        ),
    ]
