# Generated by Django 4.2 on 2023-05-05 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_alter_userprofile_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='initial_balance',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=1000, max_digits=10),
        ),
    ]