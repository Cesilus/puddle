from django import forms

from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image',)
        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }
# item/forms.py


class PurchaseForm(forms.Form):
    full_name = forms.CharField(label='Full Name', max_length=100, required=True)
    email = forms.EmailField(label='Email', required=True)
    address = forms.CharField(label='Address', max_length=200, required=True)
    city = forms.CharField(label='City', max_length=100, required=True)
    state = forms.CharField(label='State', max_length=100, required=True)
    zip_code = forms.CharField(label='ZIP Code', max_length=10, required=True)
    name_on_card = forms.CharField(label='Name on Card', max_length=100, required=True)
    card_number = forms.CharField(label='Credit Card Number', max_length=16, required=True)
    exp_month = forms.CharField(label='Expiration Month', max_length=20, required=True)
    exp_year = forms.CharField(label='Expiration Year', max_length=4, required=True)
    cvv = forms.CharField(label='CVV', max_length=4, required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        # Add custom email validation here
        if not email.endswith('@example.com'):
            self.add_error('email', 'Please enter a valid email address ending with @example.com')

        card_number = cleaned_data.get("card_number")
        # Add custom credit card validation here
        if not card_number.startswith('1234'):
            self.add_error('card_number', 'Please enter a valid credit card number')
