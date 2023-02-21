from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify


class BaseModel(models.Model):
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Base model'


class Category(BaseModel):
    name = models.CharField(
        max_length=255,
        verbose_name='Category name'
    )
    slug = models.SlugField(
        null=True,
        blank=True,
        unique=True
    )
    description = models.CharField(
        max_length=255,
        verbose_name='Category description'
    )

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'Category'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Product(BaseModel):
    category = models.ManyToManyField(
        to=Category
    )
    name = models.CharField(
        max_length=255,
        verbose_name='Product name'
    )
    slug = models.SlugField(
        unique=True,
        null=True, blank=True
    )
    description = models.TextField(
        verbose_name='Product description'
    )
    price = models.DecimalField(
        verbose_name='Product price',
        max_digits=10,
        decimal_places=2
    )

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        db_table = 'Product'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    

class Inventory(BaseModel):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE
    )
    stock_status = models.BooleanField(
        verbose_name='Stock status'
    )
    quantity = models.PositiveBigIntegerField(
        verbose_name='Quantity',
        default=0
    )

    class Meta:
        verbose_name = 'Invertory'
        verbose_name_plural = 'Invertories'
        db_table = 'Invertory'

    def __str__(self):
        return self.product.name
    

class ProductImages(BaseModel):
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE
    )
    thumbnail_pc = models.ImageField(
        verbose_name='Thumbnail picture',
        upload_to='products/%Y/%m/%d',
        null=True, blank=True
    )
    large_pc = models.ImageField(
        verbose_name='Large picture',
        upload_to='products/%Y/%m/%d',
        null=True, blank=True
    )

    class Meta:
        verbose_name = 'ProductImage'
        verbose_name_plural = 'ProductImages'
        db_table = 'ProductImage'

    def __str__(self):
        return self.product.name
    

class Customer(BaseModel):
    full_name = models.CharField(
        max_length=255,
        verbose_name='Full name'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name='Phone number'
    )
    address = models.CharField(
        max_length=255,
        verbose_name='Address'
    )

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'
        db_table = 'Customer'

    def __str__(self):
        return self.full_name
    

class Order(BaseModel):
    customer = models.ForeignKey(
        to=Customer,
        on_delete=models.CASCADE
    )
    product = models.ManyToManyField(
        to=Product
    )
    total_price = models.CharField(
        max_length=255,
        verbose_name='Total price'
    )

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
        db_table = 'Order'

    def __str__(self):
        return self.customer.full_name