# Generated by Django 3.0.2 on 2020-05-10 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0003_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='sid',
            field=models.IntegerField(unique=True),
        ),
    ]
