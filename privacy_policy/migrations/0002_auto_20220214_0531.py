# Generated by Django 3.0.4 on 2022-02-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('privacy_policy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='heading',
            field=models.CharField(max_length=256),
        ),
    ]
