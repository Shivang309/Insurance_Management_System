# Generated by Django 5.0.4 on 2024-05-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Insurance', '0013_alter_appointment_status_alter_customerdetail_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('A', 'Accepted'), ('R', 'Rejected')], default='P', max_length=10),
        ),
    ]
