from django import forms
from .models import Product, Category, SizeProduct


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','price','description','category','image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title','description']

class SizeProductForm(forms.ModelForm):
    class Meta:
        model = SizeProduct
        fields = ['product','horizontal','vertical']
