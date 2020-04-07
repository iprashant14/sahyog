from django.db import models
from django.utils import timezone

from utils.helpers import upload_image


# Create your models here.


class Beneficiary(models.Model):
    image = models.ImageField(upload_to=upload_image)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Beneficiaries"

    def __str__(self):
        return f"{self.created}"

    @classmethod
    def get_results_by_date(cls, date):
        today = timezone.now().today()
        tomorrow = today + timezone.timedelta(days=1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        return cls.objects.filter()
