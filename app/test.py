# test nhu 1 chuyen gia
# django tips from Sang Nguyen

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

import django

django.setup()


from category.api.serializers import CustomCategorySerializer
from category.models import Category
from taikhoan.models import Taikhoan as User

user = User.objects.first()
category = Category.objects.create(name="test 2", owner=user)
# serializer = CustomCategorySerializer(categorys)

# print(serializer.data)
