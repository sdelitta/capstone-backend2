# Generated by Django 4.0.4 on 2022-05-09 17:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petpursuit', '0008_rename_user_canine_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='canine',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='feline',
            old_name='user_id',
            new_name='user',
        ),
    ]