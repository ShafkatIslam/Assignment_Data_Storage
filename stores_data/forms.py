from django import forms
from django.contrib.auth.models import User
from .models import User


class ParentForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    street = forms.CharField(label='Street:',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    city = forms.CharField(label='City:',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.CharField(label='State:',  widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip = forms.CharField(label='Zip:',widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'street', 'city', 'state', 'zip')

class ChildForm(forms.ModelForm):
    first_name = forms.CharField(label='First Name:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    belong_to = forms.CharField(label='Parent(Belong to):',  widget=forms.TextInput(attrs={'class': 'form-control'}))


    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'belong_to')
