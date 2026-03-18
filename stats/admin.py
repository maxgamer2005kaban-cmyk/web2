from django.contrib import admin
from .models import Director, VideoProduct, ProductType

@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'birth_year')
    search_fields = ('full_name',)

@admin.register(VideoProduct)
class VideoProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'product_type', 'release_year')
    search_fields = ('title', 'product_type')
    list_filter = ('product_type', 'release_year')
