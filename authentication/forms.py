#!coding:utf-8
from django import forms
from django.contrib.auth.models import User


class SigninForm(forms.Form):
    error_messages = {
        'user_not_exist':'username can not be empty',
        'password_empty':'password can not be empty'
    }
    username = forms.CharField(required=True, max_length=20, strip=True, 
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username'}))
    password = forms.CharField(required=True, max_length=20, min_length=6, 
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter your password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        user = User.objects.filter(username=username)
        if not user:
            raise forms.ValidationError(self.error_messages['user_not_exist'])
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if password == '':
            raise forms.ValidationError(self.error_messages['password_empty'])
        return password


class SignupForm(forms.Form):
    error_messages = {
        'email_exist':'该邮箱已被注册！',
        'password_different':'两次输入的密码不一致',
        'username_short':'用户名至少3个字符'
    }
    email = forms.EmailField(required=True, 
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    username = forms.CharField(required=True, 
        widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(required=True, 
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(required=True, 
        widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exist = User.objects.filter(email=email)
        if email and email_exist:
            raise forms.ValidationError(self.error_messages['email_exist'])
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError(self.error_messages['username_short'])

    def clean_password2(self):
        email = self.cleaned_data.get('email')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.error_messages['password_different'])
        return password2

        