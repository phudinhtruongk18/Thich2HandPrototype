from django.urls import reverse
from django.db import models
from taikhoan.models import Taikhoan

# Create your models here.

class ToolCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cate_image = models.ImageField(upload_to='photos/toolcategory/', blank=True)

    class Meta:
        verbose_name = 'toolcategory'
        verbose_name_plural = 'toolcategories'

    def get_url(self):
        return reverse('tools_by_category', args=[self.slug])

    def __str__(self):
        return self.name

class Tool(models.Model):
    category = models.ForeignKey(ToolCategory, on_delete=models.CASCADE)  # Khi xóa category thì tool bị xóa
    name = models.CharField(max_length=200, unique=True,null=False)
    link = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/tools/')
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('tool_detail', args=[self.category.slug, self.slug])

    def get_embed(self):
        embeb = self.link
        try:
            embeb = embeb.replace("watch?v=", "embed/")
        except Exception as e:
            print(e,"<- exception")
            embeb = self.link
        return embeb


    def __str__(self):
        return self.name


class ToolReviewRating(models.Model):
    product = models.ForeignKey(Tool, on_delete=models.CASCADE)
    user = models.ForeignKey(Taikhoan, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
