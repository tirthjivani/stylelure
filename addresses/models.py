from django.db import models
from django_countries.fields import CountryField
from billing.models import BillingProfile

ADDRESS_TYPES = (
    ('billing', 'Billing'),
    ('shipping', 'Shipping'),
)

class Address(models.Model):
    billing_profile  = models.ForeignKey(BillingProfile)
    first_name       = models.CharField(max_length=30 ,blank=True,null=True)
    last_name        = models.CharField(max_length=30,blank=True,null=True)
    address_type     = models.CharField(max_length=120, choices=ADDRESS_TYPES)
    phone_number     = models.CharField(max_length=15)
    address_line_1   = models.CharField(max_length=256, blank=True,null=True,)
    address_line_2   = models.CharField(max_length=256,null=True, blank=True)
    city 			 = models.CharField(max_length=120, blank=True)
    state 			 = models.CharField(max_length=128, blank=True)
    postal_code   	 = models.CharField(max_length=20, blank=True)
    country   		 = CountryField()

    def __str__(self):
        return str(self.billing_profile)

    def get_id(self):
        return self.id

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_address(self):
        return "{line1}\n{line2}\n{city}\n{state}, {postal}\n{country}".format(
                line1 = self.address_line_1,
                line2 = self.address_line_2 or "",
                city = self.city,
                state = self.state,
                postal= self.postal_code,
                country = self.country
            )
