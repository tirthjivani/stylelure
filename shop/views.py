from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from Products.models import Product
from cart.models import Cart



def index(request):
    featured_product = Product.objects.all().featured()
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    context={
    "featured_product":featured_product,
    "cart":cart_obj
    }
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        tel=request.POST.get('tel')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        try:
            send_mail(subject, message, email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect('success')
    return render(request, 'index.html', context)

def cart(request):
    return render(request,'cart.html')

# def checkout(request):
#     form=AddressForm
#     return render(request,'checkout.html',{'form':form})

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['first_name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "Contact.html", {'form': form})


def successView(request):
    return HttpResponse('Success! Thank you for your message.')


# Create your views here.
