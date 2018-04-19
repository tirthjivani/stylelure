from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField(max_length=10, label='First Name')
    last_name = forms.CharField(max_length=10, label='Last Name')
    phone_number = forms.RegexField(
        regex='^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6-9]\d{9}$')
    email = forms.CharField(max_length=254, required=True,
                            widget=forms.EmailInput())
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}),
        max_length=4000,
        help_text='The max length of the message is 4000.')
