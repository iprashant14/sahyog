from decimal import Decimal

from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models
from django.db.models import Sum
from django.db.models.functions import Coalesce
from image_cropping import ImageRatioField
from image_cropping.utils import get_backend
from utils.helpers import upload_image


# Create your models here.


class Benefactor(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.CharField(max_length=10, validators=[MinLengthValidator(10)], unique=True)
    image = models.ImageField(default='default_benefactor_image.jpg', upload_to=upload_image)
    cropping = ImageRatioField('image', '255x255')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name :- {self.name} | Mobile:- {self.mobile} "

    @property
    def amount(self):
        return self.transaction_set.aggregate(total_amount=Coalesce(Sum('amount'), Decimal('0.00')))["total_amount"]

    @property
    def thumbnail_url(self):
        return get_backend().get_thumbnail_url(
            self.image,
            {
                'size': (255, 255),
                'box': self.cropping,
                'crop': True,
                'detail': True,
                'scale': 0.5
            }
        )


class BenefactorTransaction(models.Model):
    benefactor = models.ForeignKey(Benefactor, null=True, on_delete=models.SET_NULL, related_name='transaction_set')
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.benefactor} | Amount :- Rs {self.amount} /-"
