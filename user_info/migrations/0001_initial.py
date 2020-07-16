# Generated by Django 3.0.8 on 2020-07-16 11:15

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BulkJob',
            fields=[
                ('BID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('noOfEmployees', models.PositiveIntegerField()),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'Bulk Jobs',
                'verbose_name_plural': 'Bulk Jobs',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('CID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Individual',
            fields=[
                ('UID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(default=None, max_length=25)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('username', models.CharField(default=None, max_length=25)),
                ('contactNo', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('houseNo_flatNo', models.CharField(default='', max_length=7)),
                ('street', models.CharField(default='', max_length=20)),
                ('landmark', models.CharField(blank=True, default='', max_length=20)),
                ('city', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=20)),
                ('country', models.CharField(default='', max_length=20)),
                ('pincode', models.TextField(default='')),
                ('firstName', models.CharField(default=None, max_length=15)),
                ('middleName', models.CharField(blank=True, max_length=15)),
                ('lastName', models.CharField(default=None, max_length=15)),
                ('profile_pic', models.FileField(blank=True, upload_to='')),
                ('DOB', models.DateField()),
                ('DOJ', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('JID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('CID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user_info.Category')),
            ],
            options={
                'verbose_name': 'Jobs',
                'verbose_name_plural': 'Jobs',
            },
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('UID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(default=None, max_length=25)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('username', models.CharField(default=None, max_length=25)),
                ('contactNo', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('houseNo_flatNo', models.CharField(default='', max_length=7)),
                ('street', models.CharField(default='', max_length=20)),
                ('landmark', models.CharField(blank=True, default='', max_length=20)),
                ('city', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=20)),
                ('country', models.CharField(default='', max_length=20)),
                ('pincode', models.TextField(default='')),
                ('organisationName', models.CharField(max_length=30)),
                ('organisationLogo', models.FileField(blank=True, upload_to='')),
                ('description', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('RID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(5.0)])),
            ],
        ),
        migrations.CreateModel(
            name='ReviewConnector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.CharField(max_length=10)),
                ('targetID', models.CharField(max_length=10)),
                ('RID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.Review')),
            ],
            options={
                'verbose_name': 'Review Connector',
                'verbose_name_plural': 'Review Connector',
            },
        ),
        migrations.CreateModel(
            name='OBJ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.BulkJob')),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.Organisation')),
            ],
            options={
                'verbose_name': 'Organisation to Bulk Job Connector',
                'verbose_name_plural': 'Organisation to Bulk Job Connector',
            },
        ),
        migrations.CreateModel(
            name='JobsAvailable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.CharField(max_length=15)),
                ('basePay', models.FloatField()),
                ('timePeriodOfService', models.DurationField()),
                ('negotiable', models.BinaryField()),
                ('DOP', models.DateField()),
                ('noOfRequiredPersonnel', models.PositiveIntegerField()),
                ('JID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.Jobs')),
            ],
            options={
                'verbose_name': 'Jobs Available',
                'verbose_name_plural': 'Jobs Available',
            },
        ),
        migrations.CreateModel(
            name='Follows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrganisationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.Organisation')),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.Individual')),
            ],
            options={
                'verbose_name': 'Follows',
                'verbose_name_plural': 'Follows',
            },
        ),
        migrations.CreateModel(
            name='FOI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UID', models.CharField(max_length=10)),
                ('JID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.Jobs')),
            ],
            options={
                'verbose_name': 'Field Of Interest',
                'verbose_name_plural': 'Field Of Interest',
            },
        ),
        migrations.CreateModel(
            name='EBJ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.BulkJob')),
                ('UID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_info.Individual')),
            ],
            options={
                'verbose_name': 'Employee to Bulk Job Connector',
                'verbose_name_plural': 'Employee to Bulk Job Connector',
            },
        ),
    ]