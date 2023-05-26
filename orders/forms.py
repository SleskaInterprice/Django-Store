from django import forms
from orders.models import Orders


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иван'}),
                                 label='Имя')
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Иванов'}),
                                label='Фамилия')
    address = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'г.Москва, ул.Срелецкая 21, кв.137'}),
        label='Адрес')
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ivan@internet.ru'}),
                            label='Email')

    class Meta:
        model = Orders
        fields = ('first_name', 'last_name', 'address', 'email')
