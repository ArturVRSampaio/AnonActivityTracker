from django import forms


class LoginForm(forms.Form):
    token = forms.CharField(max_length=100, label='Token')


class signinForm(forms.Form):
    alias = forms.CharField(max_length=30, label='alias')

class NewGroup(forms.Form):
    name = forms.CharField(max_length=30, label='name')
    description = forms.CharField(max_length=30, label='description')
