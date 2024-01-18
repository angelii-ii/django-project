from django import forms
from django.contrib.auth.models import User

class userRegisterForm(forms.Form):
    user_name=forms.CharField(max_length=55,widget=forms.TextInput(attrs={'placeholder':'Enter Username'}))
    email=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Email@example.com'}))
    first_name=forms.CharField(max_length=100)
    last_name=forms.CharField(max_length=100)
    password1=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Enter your password'}))
    password2=forms.CharField(max_length=20,widget=forms.PasswordInput(attrs={'placeholder':'Repeat your password'}))

    def clean_user_name(self):
        user=self.cleaned_data['user_name']
        if User.objects.filter(username=user).exists():
            raise forms.ValidationError('user exists')
        return user

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('duplicate Email')
        return email

    def clean_password_2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']
        if password1!=password2:
            raise forms.ValidationError('duplicate password')
        elif len(password2)<8:
            raise forms.ValidationError('minimum 8 characters')
        elif not any(i.isupper() for i in password2):
            raise forms.ValidationError('use at lease one capital letter')
        else:return password1

#----------------------

class userLoginForm(forms.Form):
    user= forms.CharField()
    password= forms.CharField()

#____________Changepassword

class changePasswordForm(forms.Form):
    old_password=forms.CharField(widget=forms.PasswordInput(attrs={}))
    new_password1=forms.CharField(widget=forms.PasswordInput())
    new_password2=forms.CharField(widget=forms.PasswordInput())