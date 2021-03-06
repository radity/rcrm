# Generated by Django 2.0.6 on 2018-07-16 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rcrm_contact', '0001_initial'),
        ('rcrm_account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BooleanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('boolean', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Boolean',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CharfieldModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('charfield', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Charfield',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='DateModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Date',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='DateTimeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Date Time',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Dynamic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('charfield', models.ManyToManyField(blank=True, to='rcrm_dynamic.CharfieldModel')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcrm_contact.Contact')),
                ('date', models.ManyToManyField(blank=True, to='rcrm_dynamic.DateModel')),
                ('date_time', models.ManyToManyField(blank=True, to='rcrm_dynamic.DateTimeModel')),
            ],
            options={
                'verbose_name': '*Dynamic',
            },
        ),
        migrations.CreateModel(
            name='DynamicTab',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('description', models.TextField(max_length=128)),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active?')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Is Deleted?')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcrm_account.CRMAccount')),
            ],
            options={
                'verbose_name': '*Dynamic Tab',
            },
        ),
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('file', models.FileField(upload_to='contact_dynamic/file/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'File',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('image', models.ImageField(upload_to='contact_dynamic/image/')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Image',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TextboxModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('textbox', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Text Box',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TimeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('date', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'Time',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='URLModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url', models.URLField(max_length=2048)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Added')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Last Modified')),
            ],
            options={
                'verbose_name': 'URL',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='dynamic',
            name='file',
            field=models.ManyToManyField(blank=True, to='rcrm_dynamic.FileModel'),
        ),
        migrations.AddField(
            model_name='dynamic',
            name='image',
            field=models.ManyToManyField(blank=True, to='rcrm_dynamic.ImageModel'),
        ),
        migrations.AddField(
            model_name='dynamic',
            name='tab',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rcrm_dynamic.DynamicTab'),
        ),
        migrations.AddField(
            model_name='dynamic',
            name='text_box',
            field=models.ManyToManyField(blank=True, to='rcrm_dynamic.TextboxModel'),
        ),
        migrations.AddField(
            model_name='dynamic',
            name='time',
            field=models.ManyToManyField(blank=True, to='rcrm_dynamic.TimeModel'),
        ),
        migrations.AddField(
            model_name='dynamic',
            name='url',
            field=models.ManyToManyField(blank=True, to='rcrm_dynamic.URLModel'),
        ),
        migrations.AddField(
            model_name='dynamic',
            name='yes_no',
            field=models.ManyToManyField(blank=True, to='rcrm_dynamic.BooleanModel'),
        ),
    ]
