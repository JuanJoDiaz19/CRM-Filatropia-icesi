# Generated by Django 4.2.6 on 2023-10-16 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_app', '0015_meeting_meeting_type_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image_link',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
