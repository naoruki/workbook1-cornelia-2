from django.db import models
CATEGORIES_LIST = [
    ('starters', 'Starters'),
    ('mains', 'Mains'),
    ('beverages', 'Beverages'),
    ('desserts', 'Desserts'),
]
class Category_list(models.Model):
    category = models.CharField(max_length=10, choices=CATEGORIES_LIST) 
    def __str__(self):
		    return self.category
            
class Product(models.Model):
    product_name = models.CharField(max_length=255)
    price = models.FloatField()
    image_url = models.CharField(max_length=2083)
    category = models.ForeignKey(Category_list,null=True, on_delete= models.SET_NULL)



