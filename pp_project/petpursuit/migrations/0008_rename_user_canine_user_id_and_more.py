# Generated by Django 4.0.4 on 2022-05-09 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petpursuit', '0007_alter_canine_user_alter_feline_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='canine',
            old_name='user',
            new_name='user_id',
        ),
        migrations.RenameField(
            model_name='feline',
            old_name='user',
            new_name='user_id',
        ),
    ]
