# Generated by Django 2.0.6 on 2018-07-12 14:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rcrm_contact', '0002_auto_20180706_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('on_off_charfield', models.BooleanField(default=False, verbose_name='Text Input')),
                ('charfied_name', models.CharField(blank=True, max_length=256, null=True)),
                ('charfied', models.CharField(blank=True, max_length=256, null=True)),
                ('on_off_textbox', models.BooleanField(default=False, verbose_name='Text Box')),
                ('textbox_name', models.CharField(blank=True, max_length=256, null=True)),
                ('textbox', models.TextField(blank=True, null=True)),
                ('on_off_image', models.BooleanField(default=False, verbose_name='Image')),
                ('image_name', models.CharField(blank=True, max_length=256, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='contact_dynamic/', verbose_name='Image')),
                ('on_off_file', models.BooleanField(default=False, verbose_name='File')),
                ('file_name', models.CharField(blank=True, max_length=256, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='contact_dynamic/', verbose_name='Image')),
                ('on_off_date_time', models.BooleanField(default=False, verbose_name='Date & Time')),
                ('date_time_name', models.CharField(blank=True, max_length=256, null=True)),
                ('date_time', models.DateTimeField(blank=True, null=True, verbose_name='Date & Time')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcrm_contact.Contact')),
            ],
        ),
    ]