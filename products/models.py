from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        """"
        Allows you to have a user friendly name in thr admin.
        """

        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    make = models.CharField(max_length=254)
    model = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=9, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):

    class Meta:
        """"
        Allows you to have a user friendly name in the admin.
        """

        verbose_name_plural = 'Product Reviews'

    product = models.ForeignKey(
        Product,
        related_name="reviews",
        on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=200)
    review = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.customer_name, self.date_added)
