from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    img_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='category'
    )
    img_url = models.URLField(blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    full_name = models.CharField(max_length=254)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    date = models.DateField()
    time = models.TimeField()
    number_of_people = models.IntegerField()
    message = models.TextField(blank=True)
    child_seat = models.BooleanField(default=False)

    def __str__(self):
        return self.name
