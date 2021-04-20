from django import forms
from main.models import Order


class OrderForm(forms.ModelForm):
    customer_name = forms.CharField(max_length=70)
    customer_phone = forms.CharField(max_length=30)
    address_from = forms.CharField(max_length=200)
    address_to = forms.CharField(max_length=200)
    in_what_time = forms.TimeField(max_length=50)

    class Meta:
        model = Order
        fields = '__all__'
