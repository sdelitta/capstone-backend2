# Generated by Django 4.0.4 on 2022-05-10 02:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petpursuit', '0010_usercanines_userfelines_canine_usercanine_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='canine',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='canines', to='petpursuit.user'),
        ),
        migrations.AlterField(
            model_name='feline',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='felines', to='petpursuit.user'),
        ),
    ]
