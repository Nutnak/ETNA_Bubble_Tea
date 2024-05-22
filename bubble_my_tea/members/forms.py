from django import forms

class RegisterForm(forms.Form):
    firstname = forms.CharField(max_length=20)
    lastname = forms.CharField(max_length=20)
    email = forms.CharField(max_length=100)
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput())
    address = forms.CharField()
    admin = forms.BooleanField(required=False)

class LoginForm(forms.Form):
    email = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

class UpdateForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    address = forms.CharField()

class ProductsForm(forms.Form):
    name = forms.CharField(max_length=70)
    description = forms.CharField()
    price = forms.IntegerField()
    extras = forms.CharField()

class DeleteProductsForm(forms.Form):
    delname = forms.CharField()