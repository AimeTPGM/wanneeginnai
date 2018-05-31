from django import forms

from .models import Restuarant

class NameForm(forms.ModelForm):

    class Meta:
        model = Restuarant
        fields = ('name',)