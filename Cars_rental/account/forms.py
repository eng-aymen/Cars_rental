from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type':'password'}))


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.TextInput(attrs={'class': 'form-control','type':'password'})) 
    password2 = forms.CharField(label='Repeat password',widget=forms.TextInput(attrs={'class': 'form-control','type':'password'}))
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
