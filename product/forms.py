from django import forms
from .models import Product,Category

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title','price','description','amount','category','image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title','description']
