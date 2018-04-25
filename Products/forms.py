from django import forms
from django.forms import ModelForm
# from django.forms.widgets import TextInput
from .models import Product

available_size_choices = (
    ('small', 'S'),
    ('medium', 'M'),
    ('large', 'L'),
    ('extraLarge', 'XL'),
)


class ProductForm(ModelForm):

    available_size  = forms.MultipleChoiceField( choices = available_size_choices)

    class Meta:
        model = Product
        fields= '__all__'
        # fields = '__all__'
        # widgets = {
        #     'color': TextInput(attrs={'type': 'color'}),
        # }