from django import forms
from django.contrib import admin

from benefactor.models import Benefactor, BenefactorTransaction

# Register your models here.


class BenefactorTransactionForm(forms.ModelForm):
    class Meta:
        model = BenefactorTransaction
        fields = ('benefactor', 'amount')
        readonly_fields = ('created',)

    def clean(self, *args, **kwargs):
        if self.initial != {}:
            raise forms.ValidationError("Can't update transaction")
        super(BenefactorTransactionForm, self).clean(*args, **kwargs)


class BenefactorTransactionAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    list_display = ('benefactor', 'amount', 'created')
    list_select_related = ('benefactor',)
    list_filter = ('benefactor',)
    search_fields = ('benefactor__mobile', 'benefactor__name')
    form = BenefactorTransactionForm


admin.site.register(Benefactor)
admin.site.register(BenefactorTransaction, BenefactorTransactionAdmin)
