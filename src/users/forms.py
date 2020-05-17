from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['name', 'national_id', 'image']

    def clean_national_id(self):
        national_id = self.cleaned_data['national_id']        
        if national_id is not None and (not national_id.isdigit() or len(national_id) != 10):
            raise forms.ValidationError("National id not valid")
        return national_id
