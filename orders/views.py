from django.shortcuts import render


def overview(request):
	billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
	return render(request,'order_overview.html',{})
# Create your views here.

