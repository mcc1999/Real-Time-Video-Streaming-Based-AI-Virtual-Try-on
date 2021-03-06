# Generated by Django 3.1.7 on 2021-03-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_room_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appID', models.CharField(default='730a447ceec841d28133f2415810742b', max_length=50, unique=True)),
                ('certification', models.CharField(default='7b0418bbd36b402eb1e32f3ae7a6a646', max_length=200, unique=True)),
                ('channel', models.CharField(max_length=8, unique=True)),
                ('host', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='meeting_token',
            field=models.CharField(blank=True, max_length=100, unique=True),
        ),
    ]
