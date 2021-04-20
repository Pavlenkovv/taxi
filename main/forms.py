from django import forms
import re


class OrderForm(forms.Form):
    customer_name = forms.CharField(max_length=70, required=True)
    customer_phone = forms.CharField(max_length=30, required=True)
    address_from = forms.CharField(max_length=200, required=True)
    address_to = forms.CharField(max_length=200, required=True)
    in_what_time = forms.TimeField(required=True)

    def clean_customer_name(self):
        customer_name = self.cleaned_data["customer_name"].strip()
        if re.search(r"[^\u0400-\u0527 \-\']", customer_name, flags=re.IGNORECASE) is not None:
            raise forms.ValidationError("Name should have cyrillic characters only")
        return customer_name

    def clean_customer_phone(self):
        customer_phone = self.cleaned_data["customer_phone"].strip()
        if re.search(r"^\+380\(\d{2}\)\d{3}\-\d{2}\-\d{2}$", customer_phone) is None:
            raise forms.ValidationError("Phone should be in +380(ХХ)ХХХ-ХХ-ХХ format")
        return customer_phone