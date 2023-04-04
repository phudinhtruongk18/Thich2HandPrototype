from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin

from .models import Taikhoan


class AccountAdmin(UserAdmin):
    list_display = (
        "email",
        "username",
        "first_name",
        "last_name",
        "last_login",
        "date_joined",
        "is_active",
    )
    list_display_links = (
        "email",
        "username",
        "first_name",
        "last_name",
    )  # Các trường có gắn link dẫn đến trang detail
    readonly_fields = ("last_login", "date_joined")  # Chỉ cho phép đọc
    ordering = ("-date_joined",)  # Sắp xếp theo chiều ngược

    # Bắt buộc phải khai báo
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Taikhoan, AccountAdmin)
