from django import forms
from tshirt.models import UserProfileInfo, Cart, Tshirt
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
class CartForm(forms.ModelForm):
    SIZE_CHOICES = (
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extra-large'),
    )
    size = forms.Select(choices=SIZE_CHOICES)
    quantity = forms.IntegerField(min_value=1,max_value=2)
    GENDER_CHOICES= (
        ('M','Male'),
        ('F','Female'),
    )
    gender = forms.Select(choices=GENDER_CHOICES)
    class Meta:
        model = Cart
        fields = ['product','quantity','size','gender']
        widgets = {
            'product':forms.HiddenInput(),
            
        }