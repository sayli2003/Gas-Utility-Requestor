# Generated by Django 5.0.7 on 2024-07-14 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_servicerequest_service_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicerequest',
            name='service_type',
            field=models.CharField(choices=[('Service Installation', 'Service Installation'), ('Service Connection', 'Service Connection'), ('Service Disconnection', 'Service Disconnection'), ('Service Inspection', 'Service Inspection'), ('Meter Reading', 'Meter Reading'), ('Billing Inquiry', 'Billing Inquiry'), ('Emergency Service', 'Emergency Service'), ('Maintenance', 'Maintenance'), ('General Inquiry', 'General Inquiry')], default='General Inquiry', max_length=100),
        ),
    ]