from django.contrib import admin

# Register your models here.
from . models import Category,Product

class CategoryAdmin(admin.ModelAdmin):
    List_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    List_display = ['name','price','stock','available','created','updated']
    List_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    List_per_page = 20
admin.site.register(Product,ProductAdmin)
