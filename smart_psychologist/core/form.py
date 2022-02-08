from django import forms
from .models import Contact

class ContactForm(forms.Form):
    class Meta:
        model = Contact
        fields  = '__all__'
        lables = {
            'full_name':'First Name',
        }
        widgets={
            'full_name' : forms.TextInput(attrs={'class':'form-control'}) ,
            'subject' : forms.TextInput(attrs={'class':'form-control'}), 
            'email' : forms.EmailInput(attrs={'class':'form-control'}) ,
            'message' : forms.Textarea(attrs={'class':'form-control'}) ,
        }