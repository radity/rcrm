# Generated by Django 2.0.6 on 2018-07-12 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rcrm_employee', '0002_auto_20180712_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialprofile',
            name='other',
            field=models.CharField(blank=True, help_text='Pinterest:@username', max_length=256, null=True, verbose_name='Other'),
        ),
    ]
