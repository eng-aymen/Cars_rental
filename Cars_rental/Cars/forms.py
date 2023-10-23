from django import forms
class EmailCarForm(forms.Form):
    name = forms.CharField(max_length=25,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
                           )
    email = forms.EmailField(
        label='Email address',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
    )
    to = forms.EmailField(label='To Email address',
        widget=forms.EmailInput(attrs={'class': 'form-control ', 'placeholder': 'To Enter email'}),
    )
    comments = forms.CharField(required=False,
                                widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Your Comment'}),)
    
