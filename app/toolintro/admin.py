from django.contrib import admin
from .models import Tool,ToolCategory,ToolReviewRating
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}  # Gợi ý trường slug theo category_name
    list_display = ('name', 'slug')

class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'created_date', 'modified_date', 'is_available')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ToolCategory, CategoryAdmin)
admin.site.register(Tool, ToolAdmin)
admin.site.register(ToolReviewRating)
