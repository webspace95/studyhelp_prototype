# Generated by Django 3.0.4 on 2022-02-14 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_edits', '0010_howweworktext_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='howweworktext',
            name='thumbnail',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
