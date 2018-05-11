from django.shortcuts import render,redirect
from .models import Address
from django.forms import ModelForm
from billing.models import BillingProfile
from .forms import AddressForm
from django.http import Http404


def checkout_address_create_view(request):
       
    if request.method == 'POST':
        form1 = AddressForm(request.POST,prefix='form1')
        form2 = AddressForm(request.POST,prefix='form2')  
        # import pdb; pdb.set_trace()
        if form1.is_valid():
            # print(request.POST)
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
            # print(request.POST)
            instance = form2.save(commit=False)
            billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
            if billing_profile is not None:
                # address_type = request.POST.get('address_type', 'shipping')
                instance.billing_profile = billing_profile
                instance.address_type = 'billing'
                instance.save()
                # request.session[address_type + "_address_id"] = instance.id
               # print(address_type + "_address_id")
                import pdb; pdb.set_trace()
                if instance.address_type != None:
                    return redirect('order:overview')
            else:
                print("Error here")
                return redirect("home")

        # else:
        #    
        #     raise Http404

    else:
        form1 = AddressForm(prefix='form1')
        form2 = AddressForm(prefix='form2')
    return render(request,"checkout.html",{"form1":form1,"form2":form2}) 


def address_update(request):   
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
                return redirect('address')

    
    return render(request,'checkout.html',{'form1':form1,'form2':form2})  
 
    
