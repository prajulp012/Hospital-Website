# Generated by Django 4.2.2 on 2023-06-14 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0004_department_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookingss',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=255, verbose_name='Patient Name')),
                ('patient_phone', models.CharField(max_length=10, verbose_name='Patient Phone')),
                ('patient_email', models.EmailField(max_length=254, verbose_name='Patient Email')),
                ('booking_date', models.DateField(verbose_name='Booking Date')),
                ('booked_on', models.DateField(auto_now=True)),
                ('doctor_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.doctor', verbose_name='Doctor Name')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]