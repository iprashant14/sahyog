from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

models.Manager
# Create your models here.
class Benefactor(models.Model):
    name = models.CharField(max_length=200)
    mobile_no = models.IntegerField(max_length=10, validators=[MinLengthValidator(10)], unique=True)
    image = models.ImageField(default='default.img')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class BenefactorTransaction(models.Model):
    benefactor = models.ForeignKey(Benefactor, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    created = models.DateTimeField(auto_now_add=True)
