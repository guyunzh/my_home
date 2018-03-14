from django import forms
from .models import UserInfo


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserInfo
        fields = ('username', 'email','telephone','qq')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password do not match.')
        return cd['password']


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('telephone', 'qq', 'birth', 'company', 'address', 'aboutme', 'photo',)


class ChangepwdForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)

