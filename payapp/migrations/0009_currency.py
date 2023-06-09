# Generated by Django 4.2 on 2023-05-05 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_alter_userprofile_balance'),
        ('payapp', '0008_rename_timestamp_payment_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='USD', max_length=3)),
                ('name', models.CharField(max_length=100)),
                ('symbol', models.CharField(max_length=3)),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('user_profile', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='currencies', to='register.userprofile')),
            ],
        ),
    ]
