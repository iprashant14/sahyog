from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Email(models.Model):
    name = models.CharField(max_length=200)
    comments = models.CharField(max_length=400)
    email = models.EmailField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Emails"

    def __str__(self):
        return f"Email :- {self.email} | Name:- {self.name} | created at :- {self.created}"