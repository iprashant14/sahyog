from django.db import models

# Create your models here.
class Beneficiary(models.Model):
    image = models.ImageField(default='default.img')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.created}"