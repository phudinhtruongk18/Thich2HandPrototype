from django.db import models

# Create your models here.


class Language(models.Model):
    language_id = models.CharField(max_length=250, blank=True)
    language_code = models.CharField(max_length=250, default="en")

    def __str__(self):
        return self.cart_id
