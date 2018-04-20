from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model,login as auth_login
from .forms import SignUpForm,AddressForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
# from .models import UserProfile

User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@method_decorator(login_required, name='dispatch')
class UserUpdateView(UpdateView):
    # model = User
    # fields['email'].widget.attrs['readonly'] = True
    # fields = ('first_name', 'last_name', 'email','country' )
    form_class = AddressForm

    # form_class.fields['email'].widget.attrs['readonly'] = True
    template_name = 'my_account.html'
    success_url = reverse_lazy('my_account')

    def get_object(self):
        return self.request.user

    # def get_initial(self):
    #     return { 'country': 'india', 'state':'Gujarat' }
