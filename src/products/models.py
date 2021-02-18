from django.db import models
import random
import os


from django.urls import reverse


def get_filename_ext(filepath):
    basename = os.path.basename(filepath)
    name, ext = os.path.splitext(basename)

    return name, ext


# Create your models here.


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 2323232)
    name, ext = get_filename_ext(filename)
    final_filename = '{title}-{new_filename}{ext}'.format(
        title=instance.title, new_filename=new_filename, ext=ext)
    print(final_filename)
    return "products/{final_filename}".format(final_filename=final_filename)


class Product(models.Model):  # name as a singular item most of the time

    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10, default=39.9)
    image = models.ImageField(upload_to=upload_image_path,
                              max_length=100, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
