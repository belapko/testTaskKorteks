# Generated by Django 4.1.7 on 2023-02-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performer',
            name='title',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
