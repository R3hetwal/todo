# Generated by Django 4.1.6 on 2023-02-07 17:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_newuser_start_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='user_name',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='newuser',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 7, 17, 37, 44, 292793, tzinfo=datetime.timezone.utc)),
        ),
    ]
