# Generated by Django 3.0.8 on 2020-07-16 06:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user_info', '0013_auto_20200716_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulkjob',
            name='BID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='CID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='JID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='review',
            name='RID',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
