# Generated by Django 2.0.6 on 2018-07-16 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcrm_dynamic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dynamictab',
            name='description',
            field=models.TextField(blank=True, max_length=128, null=True),
        ),
    ]