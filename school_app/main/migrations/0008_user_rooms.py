# Generated by Django 5.0.6 on 2024-05-29 17:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_room_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='rooms',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=30), null=True, size=None),
        ),
    ]