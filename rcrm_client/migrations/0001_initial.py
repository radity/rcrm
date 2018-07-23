# Generated by Django 2.0.6 on 2018-07-19 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rcrm_account', '0001_initial'),
        ('rcrm_contact', '0001_initial'),
        ('rcrm_util', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcrm_account.CRMAccount')),
                ('address', models.ManyToManyField(blank=True, to='rcrm_util.Address')),
                ('contact', models.ManyToManyField(blank=True, to='rcrm_contact.Contact')),
                ('email', models.ManyToManyField(blank=True, to='rcrm_util.Email')),
                ('phone', models.ManyToManyField(blank=True, to='rcrm_util.Phone')),
                ('social', models.ManyToManyField(blank=True, to='rcrm_util.SocialProfile')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
