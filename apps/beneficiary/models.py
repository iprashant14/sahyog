from django.db import models
from django.utils import timezone

from utils.helpers import upload_image


# Create your models here.


class Beneficiary(models.Model):
    image = models.ImageField(upload_to=upload_image)
    image_date = models.DateField(help_text="Image clicked date")
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Beneficiaries"

    def __str__(self):
        return f"{self.created}"

    def save(self, *args, **kwargs):
        self.image_date = self.image_date if self.image_date else self.created.date()
        super(Beneficiary, self).save(*args, **kwargs)
