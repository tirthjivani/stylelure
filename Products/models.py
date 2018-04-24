from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField

available_size_choices = (
    ('small', 'S'),
    ('medium', 'M'),
    ('large', 'L'),
    ('extraLarge', 'XL'),
)

class Category(models.Model):
    Category_name  = models.CharField(max_length=200,default='Other')
    slug  = models.SlugField(max_length=200, unique=True)


    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.Category_name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

class Product(models.Model):
    title           = models.CharField(max_length=30)
    slug            = models.SlugField(blank=True, unique=True)
    category        = models.ForeignKey(Category, related_name='products',default='Other')
    price           = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image           = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description     = models.TextField(blank=True)
    stock           = models.PositiveIntegerField(default=2)
    available_color = ColorField(default='#FF0000')
    available_size  = models.CharField(max_length=20, default='S', choices = available_size_choices)
    active          = models.BooleanField(default=True)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    sku            = models.CharField(max_length=32, unique=True,default=1)


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])



