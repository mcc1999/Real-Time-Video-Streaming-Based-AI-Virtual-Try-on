# Generated by Django 3.1.7 on 2021-03-20 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210319_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='room_num',
            field=models.CharField(blank=True, max_length=8),
        ),
    ]
