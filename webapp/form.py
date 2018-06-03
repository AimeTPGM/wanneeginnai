from django import forms

from .models import Restuarant

class RestuarantForm(forms.ModelForm):

    class Meta:
        model = Restuarant
        fields = ('name',)