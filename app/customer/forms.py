from django import forms
from django.contrib.auth.models import User
from .models import Customer

class UserUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        #TODO Learn this type of writing (above)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'pd-inp'

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class CustomerUpdateForm(forms.ModelForm):
    CHOICES = [
        ("Male", "Male"),
        ("Female", "Female")
    ]
    gender = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(attrs={'id': 'choices'}))

    def __init__(self, *args, **kwargs):
        super(CustomerUpdateForm, self).__init__(*args, **kwargs)
        #TODO Learn this type of writing (above)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs['class'] = 'pd-inp'
    
    class Meta:
        model = Customer
        fields = ['date_of_birth','gender']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}), 
        }
    
