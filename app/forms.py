from django import forms


class LoginForm(forms.Form):
    token = forms.CharField(max_length=100, label='Token')


class signinForm(forms.Form):
    alias = forms.CharField(max_length=30, label='alias')
