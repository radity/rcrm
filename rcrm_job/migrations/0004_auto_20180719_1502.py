# Generated by Django 2.0.6 on 2018-07-19 15:02

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcrm_job', '0003_auto_20180718_0805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=4096),
        ),
        migrations.AlterField(
            model_name='job',
            name='type_of_employment',
            field=models.CharField(choices=[('F', 'Full-Time'), ('P', 'Part-Time'), ('B', 'Full-Time / Part-Time')], max_length=1),
        ),
    ]