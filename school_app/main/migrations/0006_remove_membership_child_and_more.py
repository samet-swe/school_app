# Generated by Django 5.0.6 on 2024-05-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_delete_role_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='child',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='relationship',
        ),
        migrations.AddField(
            model_name='parent',
            name='childUsername',
            field=models.CharField(default='student', max_length=20),
        ),
        migrations.AddField(
            model_name='parent',
            name='relationship',
            field=models.CharField(default='parent', max_length=30),
        ),
    ]
