from django import forms
from django.utils import timezone


class CommentForm(forms.Form):
    image_date = forms.DateField(initial=timezone.now().today(), widget=forms.DateInput(attrs={'type': 'date'}))
    images = forms.ImageField()

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == "images":
                visible.field.widget.attrs['multiple'] = 'multiple'
