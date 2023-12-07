from django import forms
from .models import Category

PRODUCT_CATEGORY = list()

for i in range(Category.objects.all().count()):
    PRODUCT_CATEGORY.append((i, Category.objects.all()[i].name))

class AddProductForm(forms.Form):
    name = forms.CharField(max_length=60)
    price = forms.IntegerField()
    photo = forms.ImageField(required=False)
    description = forms.CharField()
    category = forms.TypedChoiceField(choices=PRODUCT_CATEGORY, coerce=str)