from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


# Create your models here.
class Benefactor(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10, validators=[MinLengthValidator(10)], unique=True)
    image = models.ImageField(default='default.img')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name :- {self.name} | Mobile:- {self.mobile} "

    @property
    def amount(self):
        return self.transaction_set.all


class BenefactorTransaction(models.Model):
    benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.SET_NULL, related_name='transaction_set')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.benefactor.mobile} | Amount - Rs {self.amount} /-"
