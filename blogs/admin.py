from django.contrib import admin
from . import models

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','price','popularity']
    list_editable = ['price','popularity']
    # readonly_fields = ['description','slug']
    prepopulated_fields = {'slug':['title']}
    list_filter = ['price','popularity']

class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ['color','size']
    list_editable = ['size']

class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['title','url_title']
    list_editable = ['url_title']

class ProductTagAdmin(admin.ModelAdmin):
    list_display = ['tag']

admin.site.register(models.Products,ProductAdmin)
admin.site.register(models.ProductCategory,ProductCategoryAdmin)
admin.site.register(models.ProductInfo,ProductInfoAdmin)
admin.site.register(models.ProductTag,ProductTagAdmin)