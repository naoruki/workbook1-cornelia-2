from django.urls import path
from Menu import views

urlpatterns= [
    path('',views.index,name="home"),
    path('<str:cat>/',views.categories, name="category")
]