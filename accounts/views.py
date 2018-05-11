from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model,login as auth_login
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from cart.models import Cart
from billing.models import BillingProfile
from orders.models import Order
from django.contrib.auth.forms import PasswordChangeForm
from addresses.forms import AddressForm
from addresses.models import Address

# from .models import UserProfile

User = get_user_model()


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            form = SignUpForm(request.POST)

            if form.is_valid():
                user = form.save()
                auth_login(request, user,backend='django.contrib.auth.backends.ModelBackend')
                return redirect('index')
        else:
            form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def account_view(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    order_obj, order_obj_created = Order.objects.new_or_get(billing_profile, cart_obj)
    # form = PasswordChangeForm(request.user)
    return render(request,'my_account.html',{'object':order_obj,'billing_profile':billing_profile})


# class Account_View(UpdateView):

#     template_name = 'my_account.html'
#     form_class = PasswordChangeForm(request.user)
#     second_form_class = AddressForm
#     success_url = reverse_lazy('success')

#     def get_context_data(self, **kwargs):
#         context = super(MyView, self).get_context_data(**kwargs)
#         if 'form' not in context:
#             context['form'] = self.form_class(initial={'user': request.user})
#         if 'form2' not in context:
#             context['form2'] = self.second_form_class()
#         return context

#     def get_object(self):
#         return get_object_or_404(Model, pk=self.request.session['someval'])

#     def form_invalid(self, **kwargs):
#         return self.render_to_response(self.get_context_data(**kwargs))

#     def post(self, request, *args, **kwargs):

#         # get the user instance
#         self.object = self.get_object()

#         if 'form' in request.POST:

#             # get the primary form
#             form_class = self.get_form_class()
#             form_name = 'form'

#         else:

#             # get the secondary form
#             form_class = self.second_form_class
#             form_name = 'form2'

#         # get the form
#         form = self.get_form(form_class)

#         # validate
#         if form.is_valid():
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(**{form_name: form})

# @method_decorator(login_required, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = Address
#     # fields['email'].widget.attrs['readonly'] = True
#     # fields = ('first_name', 'last_name', 'email','country' )
#     form_class = AddressForm

#     # form_class.fields['email'].widget.attrs['readonly'] = True
#     template_name = 'account-details.html'
#     success_url = reverse_lazy('account')

#     def get_object(self):
#         return self.request.user

#     def get_initial(self):
#         return { 'country': 'india', 'state':'Gujarat' }

def user_address_update(request):   
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    print(billing_profile)
    address_qs = None
    if billing_profile is not None:
        if request.user.is_authenticated():
            address_qs = Address.objects.filter(billing_profile=billing_profile) 
        try:
            shipping_address = Address.objects.get(billing_profile=billing_profile.id,address_type='shipping')
        except Address.DoesNotExist:
            print("Show message to user, Address is gone?")
            return redirect("cart:cart")
        try:   
            billing_address = Address.objects.get(billing_profile=billing_profile.id,address_type='billing') 
        except Address.DoesNotExist:
            print(" Address is gone?")
            return redirect("cart:cart")
        # shipping_address = Address.objects.get(id=27)
        # import pdb; pdb.set_trace()
        form1=AddressForm(prefix='form1',instance=shipping_address,data=request.POST or None )
        form2=AddressForm(prefix='form2',instance=billing_address,data=request.POST or None)

        if request.method=='POST':
            import pdb; pdb.set_trace()
            if form2.is_valid():
                form2.save()
            if form1.is_valid():
                form1.save()
                

    
    return render(request,'account-details.html',{'form1':form1,'form2':form2})  