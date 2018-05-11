from django import forms
# from django.contrib.auth import authenticate, login, get_user_model
from localflavor.in_.forms import INStateSelect,INStateField,INAadhaarNumberField,INZipCodeField
from django_countries.fields import CountryField
from .models import Address as Add


class AddressForm(forms.ModelForm):
    """docstring for AddressForm"""
    phone_number = forms.RegexField(
        regex='^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6-9]\d{9}$')
    state=INStateField(widget=INStateSelect())
    address_line_1=forms.CharField(widget=forms.Textarea(
            attrs={'rows': 3}),max_length=100, help_text='Please provide the number and street.')
    address_line_2=forms.CharField(widget=forms.Textarea(
            attrs={'rows': 1}),max_length=100, help_text='Please include landmark' 
        '(e.g : Opposite Bank) as the carrier service may find it easier to locate your address.')
    # aadhaar=INAadhaarNumberField()
    postal_code=INZipCodeField()
    # country=CountryField()

    class Meta:
        model   = Add
        fields  =['first_name', 'last_name', 'phone_number',
                'address_line_1','address_line_2','country','state','postal_code','city'
                  ]
