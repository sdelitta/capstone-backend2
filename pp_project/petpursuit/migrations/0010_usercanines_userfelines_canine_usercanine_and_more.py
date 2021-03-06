# Generated by Django 4.0.4 on 2022-05-09 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('petpursuit', '0009_rename_user_id_canine_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCanines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserFelines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='canine',
            name='userCanine',
            field=models.ManyToManyField(through='petpursuit.UserCanines', to='petpursuit.user'),
        ),
        migrations.AddField(
            model_name='feline',
            name='userFeline',
            field=models.ManyToManyField(through='petpursuit.UserFelines', to='petpursuit.user'),
        ),
        migrations.AddField(
            model_name='userfelines',
            name='feline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petpursuit.feline'),
        ),
        migrations.AddField(
            model_name='userfelines',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petpursuit.user'),
        ),
        migrations.AddField(
            model_name='usercanines',
            name='canine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petpursuit.canine'),
        ),
        migrations.AddField(
            model_name='usercanines',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petpursuit.user'),
        ),
    ]
