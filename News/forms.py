from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput, EmailInput,CharField
from .models import CustomerProfileModel, NewsDetailModel, Review, ContactPageModel
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
        exclude = ('user',)

class BasicCustomerForm(forms.ModelForm):
    class Meta:
        model = CustomerProfileModel
        fields = ('avatar',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('subject','review',)

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactPageModel
        fields = ['name', 'email', 'subject', 'message']

        def clean(self):
            cleaned_data = super().clean()
            name = cleaned_data.get("name")
            if len(name) < 4:
                raise forms.ValidationError('Name should be more than 4')



