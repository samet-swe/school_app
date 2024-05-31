# Generated by Django 5.0.6 on 2024-05-29 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_membership_child_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='members',
            field=models.ManyToManyField(related_name='memberOf', through='main.Membership', to='main.user'),
        ),
    ]
