from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Category_list
# Create your views here.
#main menu views
def index(request): 
  menu = Product.objects.all()
  category_list=Category_list.objects.all()
  context ={'menu':menu,'category_list':category_list}
  return render(request,'index.html', context)
# category views 
def categories (request,cat):
  menu = Product.objects.all()
  category_list=Category_list.objects.all()
  categories = Category_list.objects.get(category=cat)
  context ={'categories':categories,'menu':menu,'category_list':category_list}
  return render(request,'category.html',context)