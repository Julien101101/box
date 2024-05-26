from django import forms

from .models import Shape

class ShapeForm(forms.ModelForm):
    class Meta:
        model = Shape
        fields = ['text']
        labels = {'text': ''}

#TODO?