from django.contrib import admin

# Register your models here.

from benefactor.models import Benefactor, BenefactorTransaction

admin.site.register(Benefactor)
admin.site.register(BenefactorTransaction)

