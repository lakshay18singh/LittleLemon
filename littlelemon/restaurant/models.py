from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Menu(models.Model):
    Id = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)], primary_key=True)
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=5, decimal_places=2)
    Inventory = models.IntegerField(validators=[MaxValueValidator(99999), MinValueValidator(1)])
    def __str__(self):
        return f'{self.Title} : {str(self.Price)}, {str(self.Inventory)}'


class Booking(models.Model):
    Id = models.IntegerField(validators=[MaxValueValidator(99999999999), MinValueValidator(1)], primary_key=True)
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(validators=[MaxValueValidator(999999), MinValueValidator(1)])
    BookingDate = models.DateTimeField()
