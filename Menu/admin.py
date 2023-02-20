from django.contrib import admin
from Menu.models import Product,Category_list

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','price','category')

class CateogryAdmin(admin.ModelAdmin):
    list_display=('category',)
    
admin.site.register(Product,ProductAdmin)
admin.site.register(Category_list,CateogryAdmin)