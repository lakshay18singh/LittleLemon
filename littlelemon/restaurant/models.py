from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# Create your models here.


class Menu(models.Model):
    Id = models.AutoField( primary_key=True)
    Title = models.CharField(max_length=75, unique=True)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Description = models.CharField(max_length=300)
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'


class Booking(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(1)])
    BookingDate = models.DateField()
