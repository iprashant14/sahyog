from django.db import models

from utils.helpers import upload_image


# Create your models here.


class Beneficiary(models.Model):
    image = models.ImageField(upload_to=upload_image)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Beneficiaries"

    def __str__(self):
        return f"{self.created}"
