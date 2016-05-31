from django import forms


class SigninForm(forms.Form):
    error_messages = {
        'username_empty':'username can not be empty',
        'password_empty':'password can not be empty'
    }
    username = forms.CharField(max_length=20, strip=True, widget=forms.TextInput(attrs={'class':'form-control',
                                                                                        'placeholder':'Enter your username'}))
    password = forms.CharField(max_length=20, min_length=6, widget=forms.PasswordInput(attrs={'class':'form-control',
                                                                                              'placeholder':'Enter your password'}))

    def clean_username(self):
        username = self.cleaned_data.get('username', '')
        if username == '':
            raise forms.ValidationError(self.error_messages['username_empty'])
        return username

    def clean_password(self):
        password = self.cleaned_data.get('password', '')
        if password == '':
            raise forms.ValidationError(self.error_messages['password_empty'])
        return password
