from django.contrib import admin
from .models import Post, Product

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "published_date")
    search_fields = ("title", "content")
    list_filter = ("title", "published_date")


# admin.site.register(Post, PostAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name", "description")
    list_filter = ("name", "created_at")


# admin.site.register(Product, ProductAdmin)
