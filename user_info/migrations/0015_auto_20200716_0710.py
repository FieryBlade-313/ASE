# Generated by Django 3.0.8 on 2020-07-16 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0014_auto_20200716_0648'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ebj',
            old_name='BID',
            new_name='bulk',
        ),
        migrations.RenameField(
            model_name='ebj',
            old_name='UID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='foi',
            old_name='JID',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='foi',
            old_name='UID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='follows',
            old_name='OrganisationID',
            new_name='organisation',
        ),
        migrations.RenameField(
            model_name='jobs',
            old_name='CID',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='jobsavailable',
            old_name='JID',
            new_name='job',
        ),
        migrations.RenameField(
            model_name='jobsavailable',
            old_name='UID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='obj',
            old_name='BID',
            new_name='bulk',
        ),
        migrations.RenameField(
            model_name='obj',
            old_name='UID',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='reviewconnector',
            old_name='RID',
            new_name='rewiev',
        ),
        migrations.RenameField(
            model_name='reviewconnector',
            old_name='targetID',
            new_name='target',
        ),
        migrations.RenameField(
            model_name='reviewconnector',
            old_name='UID',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='follows',
            name='UID',
        ),
        migrations.AddField(
            model_name='follows',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='user_info.Individual'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bulkjob',
            name='BID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='CID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='JID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='RID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
