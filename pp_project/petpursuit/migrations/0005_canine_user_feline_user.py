# Generated by Django 4.0.4 on 2022-05-09 16:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petpursuit', '0004_remove_shelter_location_canine_photo_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='canine',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='canines', to='petpursuit.user'),
        ),
        migrations.AddField(
            model_name='feline',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='felines', to='petpursuit.user'),
        ),
    ]
