from django import forms
from .models import Supplier,PurchaseProduct

class PurchaseProductForm(forms.ModelForm):
    class Meta:
        model = PurchaseProduct
        fields = ['user','supplier','product','amount','time_create','complete']
