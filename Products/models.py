from django.db import models
from django.utils import timezone
from colorfield.fields import ColorField
from django.db.models import Q
from django.urls import reverse

available_size_choices = (
    ('small', 'S'),
    ('medium', 'M'),
    ('large', 'L'),
    ('extraLarge', 'XL'),
)

class Category(models.Model):
    Category_name  = models.CharField(max_length=200,db_index=True,default='Other')
    slug  = models.SlugField(max_length=200, db_index=True,unique=True)


    class Meta:
        # ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'


    def __str__(self):
        return self.Category_name

    def get_absolute_url(self):
        return reverse('Products:product_list_by_category', args=[self.slug])



class Model_Category(models.Model):
    Model_Category_name  = models.CharField(max_length=200)
    slug  = models.SlugField(max_length=200,unique=True)


    class Meta:
        # ordering = ('name',)
        verbose_name = 'model_category'
        verbose_name_plural = 'model_categories'


    def __str__(self):
        return self.Model_Category_name

    def get_absolute_url(self):
        return reverse('Products:product_list_by_Model_category', args=[self.slug])


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)

    def search(self, query):
        lookups = (Q(title__icontains=query) |
                  Q(description__icontains=query) |
                  Q(price__icontains=query) |
                  Q(tag__title__icontains=query)
                  )
        # tshirt, t-shirt, t shirt, red, green, blue,
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().active()

    def featured(self): #Product.objects.featured()
        return self.get_queryset().featured()

    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id) # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None

    def search(self, query):
        return self.get_queryset().active().search(query)

class Product(models.Model):
    title            = models.CharField(max_length=30, db_index=True)
    slug             = models.SlugField(blank=True, db_index=True )
    category         = models.ForeignKey(Category, related_name='products',default='Other')
    model_category   = models.ForeignKey(Model_Category, related_name='model_products')
    price            = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    discounted_price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    # image         = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    short_description = models.TextField(blank=True)
    description      = models.TextField(blank=True)
    featured         = models.BooleanField(default=False)
    new_collection   = models.BooleanField(default=False)
    stock            = models.PositiveIntegerField(default=2)
    # available_color = ColorField(default='#FF0000')
    Manufacturer    = models.CharField(max_length=50)
    Occassion       = models.CharField(max_length=50)
    Season          = models.CharField(max_length=50)
    Gender          = models.CharField(max_length=50)
    available_size   = models.CharField(max_length=50)
    active           = models.BooleanField(default=True)
    created          = models.DateTimeField(auto_now_add=True)
    updated          = models.DateTimeField(auto_now=True)
    sku              = models.CharField(max_length=32, unique=True)

    objects = ProductManager()

    class Meta:
        ordering = ('-created',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.title

    def product_count(self):
        return Product.category.objects.count()

    def get_absolute_url(self):
        # print(reverse('Products:product_detail', args=[self.id, self.slug]))
        return reverse('Products:product_detail', args=[self.id, self.slug])

    @property
    def name(self):
        return self.title

    def id(self):
        return self.id

class ProductImages(models.Model):
    product         = models.ForeignKey(Product,related_name='images',on_delete=models.CASCADE)
    image           = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    name            = models.CharField(max_length=30,null=True,blank=True)


class ProductColors(models.Model):
    product         = models.ForeignKey(Product,related_name='colors',on_delete=models.CASCADE)
    available_color = ColorField()

    def __str__(self):
        return self.available_color
