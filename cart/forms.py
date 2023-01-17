from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 15)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int, initial=PRODUCT_QUANTITY_CHOICES[0])
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
