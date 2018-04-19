from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, get_user_model

User = get_user_model()


class SignUpForm(UserCreationForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    first_name = forms.CharField(max_length=10, label='First Name')
    last_name = forms.CharField(max_length=10, label='Last Name')
    phone_number = forms.RegexField(
        regex='^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6-9]\d{9}$')
    email = forms.CharField(max_length=254, required=True,
                            widget=forms.EmailInput())
    date_of_birth = forms.DateField(widget=forms.DateInput(
        attrs={'type': 'date'}), label='Date of Birth')
    CHOICES = [('M', 'Male'), ('F', 'Female')]
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.Select(
        attrs={"name": "select_0", "class": "form-control"}), required=True)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput,
                help_text="""• Your password cant be too similar to your other personal information.
                            <br/>• Your password must contain at least 8 characters.
                            <br/>• Your password can't be a commonly used password.
                             <br/>• Your password can't be entirely numeric""")
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput,
                                help_text='• Enter the same password as before, for verification.')
    receive_newsletter = forms.BooleanField(
        required=False, label=('  Sign Up for Newsletter'), initial=True)

    class Meta:
        model = User
        # unique_together = ('email',)
        fields = ['first_name', 'last_name', 'phone_number', 'email',
                  'gender', 'date_of_birth', 'password1', 'password2']

    # class Meta:
    #     model = User
    #     fields = ('full_name', 'email',) #'full_name',)

    # def clean_password2(self):
    #     # Check that the two password entries match
    #     password1 = self.cleaned_data.get("password1")
    #     password2 = self.cleaned_data.get("password2")
    #     if password1 and password2 and password1 != password2:
    #         raise forms.ValidationError("Passwords don't match")
    #     return password2

    # def save(self, commit=True):
    #     # Save the provided password in hashed format
    #     user = super(RegisterForm, self).save(commit=False)
    #     user.set_password(self.cleaned_data["password1"])
    #     user.is_active = False # send confirmation email via signals
    #     # obj = EmailActivation.objects.create(user=user)
    #     # obj.send_activation_email()
    #     if commit:
    #         user.save()
    #     return user

# class SignUpForm(UserCreationForm):
#     first=forms.CharField(max_length=10,label='First Name')
#     last=forms.CharField(max_length=10,label='Last Name')
#     phone= forms.RegexField(regex='^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[6-9]\d{9}$')
#     email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
#     date=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}),label='Date of Birth')
#     CHOICES=[('m','Male'),('f','Female')]
#     gender = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={"name": "select_0","class": "form-control"}),required=True)
#     receive_newsletter = forms.BooleanField(required=False,label=('  Sign Up for Newsletter'),initial=True)


#     class Meta:
#         model = User
#         unique_together = ('email',)
#         fields = ('first','last','phone','email','date','gender', 'password1', 'password2')
