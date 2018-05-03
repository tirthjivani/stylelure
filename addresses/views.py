from django.shortcuts import render,redirect
from .models import Address

from billing.models import BillingProfile
from .forms import AddressForm
from django.http import Http404


def checkout_address_create_view(request):

    if request.method == 'POST':
        form1 = AddressForm(request.POST,prefix='form1')
        form2 = AddressForm(request.POST,prefix='form2')  
        # import pdb; pdb.set_trace()
        if form1.is_valid():
            print(request.POST)
            instance = form1.save(commit=False)
            billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
            print('hii',billing_profile)
            if billing_profile is not None:
                # address_type = request.POST.get('address_type', 'shipping')
                instance.billing_profile = billing_profile
                instance.address_type = 'shipping'
                instance.save()
                # request.session[address_type + "_address_id"] = instance.id
                #print(address_type + "_address_id")
            else:
                print("Error here")
                return redirect("home")

        if form2.is_valid():
            print(request.POST)
            instance = form2.save(commit=False)
            billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
            if billing_profile is not None:
                # address_type = request.POST.get('address_type', 'shipping')
                instance.billing_profile = billing_profile
                instance.address_type = 'billing'
                instance.save()
                # request.session[address_type + "_address_id"] = instance.id
               # print(address_type + "_address_id")
            else:
                print("Error here")
                return redirect("home")

        # else:
        #     # Do something in case if form is not valid
        #     raise Http404

    else:
        form1 = AddressForm(prefix='form1')
        form2 = AddressForm(prefix='form2')
    return render(request,"checkout.html",{"form1":form1,"form2":form2}) 