# Generated by Django 4.2.2 on 2023-07-04 06:15

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('Id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(1)])),
                ('Title', models.CharField(max_length=75, unique=True)),
                ('Price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Description', models.CharField(default='No Data', max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('No_of_guests', models.IntegerField(validators=[django.core.validators.MaxValueValidator(999999), django.core.validators.MinValueValidator(1)])),
                ('BookingDate', models.DateField()),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
