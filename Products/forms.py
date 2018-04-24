from django.forms import ModelForm
from django.forms.widgets import TextInput
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }