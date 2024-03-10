from django import forms
from django.contrib.auth.models import User
from ..models import CustomerProfileModel, NewsDetailModel
class BasicUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','email',)

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email',)

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomerProfileModel
        fields = ('avatar',)




class NewsDetailForm(forms.ModelForm):
    class Meta:
        model = NewsDetailModel
        fields = '__all__'

class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerProfileModel
        fields = ('avatar',)