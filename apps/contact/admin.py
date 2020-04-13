from django.contrib import admin
from django import forms

# Register your models here.
from contact.models import Email

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('name','comments','email')
        readonly_fields = ('name','comments','email','created')

    def clean(self, *args, **kwargs):
        if self.initial != {}:
            raise forms.ValidationError("Can't update value")
        super(EmailForm, self).clean(*args, **kwargs)


class EmailAdmin( admin.ModelAdmin):
    readonly_fields = ('name','comments','email','created')

admin.site.register(Email,EmailAdmin)