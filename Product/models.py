from django.db import models

# Create your models here.
class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField()
    category = models.CharField(max_length=50)
    slug = models.SlugField(null=True)
    description = models.TextField()
    rating = models.CharField(max_length=5)
    detail = models.TextField()
    location = models.TextField()
    image = models.ImageField(upload_to="profile-images", blank=True)

    def __str__(self):
        return self.title