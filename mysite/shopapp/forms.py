from django import forms
from django.forms import ClearableFileInput

from shopapp.models import Product

class MultiplyFileInput(ClearableFileInput):
    allow_multiple_selected = True


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "name", "price", "description", "discount", "preview"

    images = forms.ImageField(
        widget=MultiplyFileInput(attrs={"multiple": True}),
    )


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
