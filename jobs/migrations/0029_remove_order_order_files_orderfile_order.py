# Generated by Django 4.0.3 on 2022-04-18 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0028_alter_order_id_alter_orderfile_id_alter_sample_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_files',
        ),
        migrations.AddField(
            model_name='orderfile',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.order'),
        ),
    ]
